#!/usr/bin/env python3
"""
canon-check.py — Canon Integrity Registry checker for the PUSH package.

Scans downstream documents for contradictions against the canon facts
manifest (`.sandcastle/canon-facts.json`). The Prop Bible is the single
source of truth; this script makes that boundary machine-checkable.

Usage:
    python3 scripts/canon-check.py                 # check whole tree
    python3 scripts/canon-check.py --changed-only  # check git-changed .md files
    python3 scripts/canon-check.py --json          # machine-readable output

Exit code 0 = clean, 1 = contradictions found, 2 = error (missing manifest,
unreadable file, etc.).

Design notes:
- Only discrete, enumerable facts are checked (per issue #19 scope). Prose is
  not parsed.
- The manifest is the SINGLE place to edit a canonical fact. To change a fact,
  edit `.sandcastle/canon-facts.json`, then run this script to find every
  downstream occurrence that needs updating.
- The Prop Bible itself and the manifest are never checked (they are the
  source). `working/` is excluded (scratch space, not canon).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / ".sandcastle" / "canon-facts.json"

# Directories scanned for contradictions. The Prop Bible (the source of truth)
# and the manifest are excluded by construction.
SCAN_DIRS = [
    "01_screenplay",
    "02_production",
    "03_ai_video",
    "04_storyboard",
    "docs",
]

# Files that are canonical sources or non-canon scratch — never checked.
EXCLUDE_FILES = {
    "02_production/prop_bible.md",  # the source of truth itself
    "02_production/RISE_MOVE_INTERNAL_v1.0.md",  # internal brainstorming, explicitly non-canonical
    "02_production/Bed_design_memo.md",  # design history, explicitly retains superseded content
}
EXCLUDE_DIRS = {"working"}


def load_manifest() -> dict:
    """Load and validate the canon facts manifest."""
    if not MANIFEST_PATH.exists():
        print(f"error: manifest not found at {MANIFEST_PATH}", file=sys.stderr)
        sys.exit(2)
    with MANIFEST_PATH.open(encoding="utf-8") as fh:
        manifest = json.load(fh)
    if "facts" not in manifest or not isinstance(manifest["facts"], list):
        print("error: manifest missing 'facts' array", file=sys.stderr)
        sys.exit(2)
    return manifest


def collect_files(changed_only: bool) -> list[Path]:
    """Collect the .md files to scan."""
    if changed_only:
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", "--diff-filter=ACMR", "HEAD"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
        except subprocess.CalledProcessError:
            # Fall back to whole tree if git is unavailable (e.g. shallow CI checkout)
            changed_only = False
        else:
            changed = {Path(p) for p in result.stdout.splitlines() if p.endswith(".md")}
            if not changed:
                return []
            return [REPO_ROOT / p for p in sorted(str(p) for p in changed)]

    files: list[Path] = []
    for d in SCAN_DIRS:
        base = REPO_ROOT / d
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            rel = p.relative_to(REPO_ROOT).as_posix()
            if rel in EXCLUDE_FILES:
                continue
            if any(part in EXCLUDE_DIRS for part in p.parts):
                continue
            files.append(p)
    return sorted(files)


def check_fact(fact: dict, text: str, rel_path: str, findings: list[dict]) -> None:
    """Check one fact against one document's text."""
    fid = fact.get("id", "?")
    kind = fact.get("kind", "assertion")
    label = fact.get("label", fid)

    def add(match: str, line: int, detail: str) -> None:
        findings.append(
            {
                "fact": fid,
                "label": label,
                "file": rel_path,
                "line": line,
                "match": match,
                "detail": detail,
            }
        )

    lines = text.splitlines()

    if kind == "enum":
        # For enum facts, flag any known-wrong token. The manifest's `values`
        # are canonical; anything that looks like a variant of the fact but is
        # not in `values` is a contradiction.
        values = fact.get("values", [])
        wrong_tokens = fact.get("wrong_tokens", [])
        for token in wrong_tokens:
            for i, line in enumerate(lines, 1):
                if token.lower() in line.lower():
                    add(token, i, f"non-canonical token '{token}' (canonical: {', '.join(values)})")

        # Pattern check: catch renamed enum members generically (e.g. a state
        # renamed to 'TACO'). Any match of the pattern whose value is not in
        # the canonical set is a contradiction. Case-sensitive: canonical usage
        # is uppercase ('STATE ONE'), so lowercase prose ('state machine',
        # 'state at') never matches.
        pattern = fact.get("pattern")
        if pattern:
            rx = re.compile(pattern["regex"])
            canonical = {c for c in pattern.get("canonical", [])}
            for i, line in enumerate(lines, 1):
                for m in rx.finditer(line):
                    val = m.group(1) if m.lastindex else m.group(0)
                    if val not in canonical:
                        add(m.group(0), i, pattern.get("detail", f"non-canonical value '{val}'"))

    elif kind == "assertion":
        # Assertion facts: forbidden tokens must not appear anywhere. Tokens
        # are matched as whole words (word-boundary aware) so that a forbidden
        # token like "Marcus's PUSH" does not false-positive on the canonical
        # "Marcus's PUSH+".
        forbidden = fact.get("forbidden", [])
        for token in forbidden:
            if not token:
                continue
            # Escape regex metachars, then require a word boundary after the
            # final word char so "PUSH" doesn't match inside "PUSH+" (the '+'
            # is not a word char, so exclude it explicitly).
            rx = re.compile(r"(?<!\w)" + re.escape(token) + r"(?![\w+])", re.IGNORECASE)
            for i, line in enumerate(lines, 1):
                if rx.search(line):
                    add(token, i, f"forbidden token '{token}' (canonical: {fact.get('value', '?')})")

        # required_in: if a doc echoes the fact (matches any marker), it must
        # contain the exact canonical value. Catches paraphrased taglines.
        required_in = fact.get("required_in")
        if required_in:
            markers = required_in.get("markers", [])
            canonical_value = fact.get("value", "")
            if canonical_value and any(m.lower() in text.lower() for m in markers):
                if canonical_value.lower() not in text.lower():
                    # Find the line containing the marker to report a useful location
                    for i, line in enumerate(lines, 1):
                        if any(m.lower() in line.lower() for m in markers):
                            add(markers[0], i, required_in.get("detail", f"paraphrase of '{canonical_value}'"))
                            break


def main() -> int:
    parser = argparse.ArgumentParser(description="Canon Integrity Registry checker")
    parser.add_argument("--changed-only", action="store_true", help="only check git-changed .md files")
    parser.add_argument("--json", action="store_true", help="machine-readable JSON output")
    args = parser.parse_args()

    manifest = load_manifest()
    facts = manifest["facts"]
    files = collect_files(args.changed_only)

    findings: list[dict] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"error: cannot read {path}: {exc}", file=sys.stderr)
            sys.exit(2)
        rel = path.relative_to(REPO_ROOT).as_posix()
        for fact in facts:
            check_fact(fact, text, rel, findings)

    if args.json:
        print(json.dumps({"files_scanned": len(files), "findings": findings}, indent=2))
    else:
        if findings:
            print(f"canon-check: {len(findings)} contradiction(s) found across {len(files)} file(s):")
            for f in findings:
                print(f"  [{f['fact']}] {f['file']}:{f['line']} — {f['detail']}")
            print("\nFix: edit the canonical fact in .sandcastle/canon-facts.json, then update")
            print("every downstream occurrence listed above. See README 'Document Hierarchy'.")
            return 1
        print(f"canon-check: clean — {len(files)} file(s) scanned, 0 contradictions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())