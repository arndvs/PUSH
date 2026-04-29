# RISE Technologies — Complete Intelligence Report

> Generated April 23, 2026 — Deep exploration across `rise-awake` and `push` codebases.

---

## Executive Summary

**RISE Technologies, Inc.** is a fully realized fictional company operating as the in-universe corporate entity behind two interconnected creative projects: **riseawake.com** (an interactive satirical product website) and **PUSH** (a ~5–7 minute comedy short film). The fictional world is built with extraordinary depth — investor relations, legal documents, internal security posture, product history, financial data, and leadership bios — all played completely straight. The comedy is never in the writing _being_ funny. It's in the writing being _perfectly earnest_ about something absurd.

---

## The Company

|                 |                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Name**        | RISE Technologies, Inc. (stylized: RISE)                                                                          |
| **HQ**          | San Francisco, California                                                                                         |
| **Domain**      | riseawake.com                                                                                                     |
| **Tagline**     | "For People Who Need A Little Push."                                                                              |
| **Founded**     | 2009 (implied by product history)                                                                                 |
| **CEO**         | Dr. Eleanor Voss — PhD Behavioral Sleep Science, Stanford                                                         |
| **Core Thesis** | The problem isn't information or intention. It's the moment between deciding and doing. RISE removes that moment. |

### Leadership Team

| Name                 | Title                 | Notable Detail                                                        |
| -------------------- | --------------------- | --------------------------------------------------------------------- |
| **Dr. Eleanor Voss** | Founder & CEO         | Has used The Push every morning since 2021. Has not been late once.   |
| **Dr. Mara Chen**    | Chief Product Officer | Architect of Push Mode. Holds 11 of 23 patents.                       |
| **James Park**       | General Counsel       | Former FTC regulatory counsel.                                        |
| **Thomas Ellery**    | CFO                   | Former Goldman Sachs. Managing S-1 process.                           |
| **Arvin**            | Former Developer      | Left August 2024. Built the internal systems. Never built the toggle. |

---

## Product Line — The Full Arc

The product history tells a 15-year story of escalating commitment. Every failed product taught RISE one lesson: _people will adapt to anything gentle._

### The Graveyard (2011–2019) — 13 Discontinued Products

| Year | Product                | Lesson Learned                                                                 |
| ---- | ---------------------- | ------------------------------------------------------------------------------ |
| 2011 | RISE Ambient           | One blackout curtain renders it irrelevant                                     |
| 2011 | RISE Tone              | Users slept _better_. Became a white noise machine                             |
| 2012 | RISE Thermal           | Users found the warm center and stayed                                         |
| 2012 | RISE Gradient          | Users can sleep at 45°                                                         |
| 2012 | RISE Alarm             | 94% slept through it                                                           |
| 2013 | RISE NudgeSense        | Phone on nightstand. User asleep                                               |
| 2013 | RISE NudgeLight        | App got 4.8★. Product got 2.1★                                                 |
| 2014 | RISE NudgeWarm         | Users still find the warm center                                               |
| 2014 | RISE NudgeTone         | Made users sleep 23 minutes _longer_                                           |
| 2015 | RISE NudgeEdge         | 100% rolled back to center                                                     |
| 2016 | RISE NudgeBar          | 74% compliance. Cult following. Not good enough                                |
| 2019 | **RISE Nudge (RN-01)** | Consolidated line. 7-stage passive tensioning. Discontinued → replaced by Push |

### Current Product: The PUSH (Model RP-01)

**Status:** Sold out. 340,000 waitlist.

The Push doesn't suggest. It delivers. The base transitions to vertical and autonomously routes the user through their morning — bathroom → closet → kitchen → departure — then returns home alone.

**Key Features:**

- **Push Mode** — Non-interruptible. "This is a feature, not a limitation."
- **Autonomous Sheet Tensioning** — Makes the bed while you're in the shower
- **Pillow Restoration Node** — Pneumatic re-centering
- **Precision Caster Navigation** — Near-silent autonomous room mapping
- **Solo Return Commute** — The bed goes home by itself
- **PM-1 Remote** — One button. One function. No off switch.

**Specs:**

- 2,048 pressure sensors (64×32 grid)
- Pneumatic nodes
- 8-meter audio pickup
- 30-min pre-activation recording
- Occupancy detection
- Relationship status inference

**Compliance Rate:** 98% (vs. 74% for the Nudge)

### Future: The PUSH Pro

"We are not currently accepting questions about The Push Pro."

### Future: The MOVE

Autonomous **vertical** navigation. Navigates stairs. Both directions. Requires Vertical Navigation Services (VNS) subscription. No timeline. No price. No loyalty discount for Push owners.

**Dr. Voss:** _"We are aware of the stairs. All of them. Both directions. We are doing something about it."_

**VNS Lapse Scenario:** The bed stops at the bottom of the stairs and waits. The user goes up alone. _"This is the most RISE scenario the product line has yet produced."_

---

## Financials (Fictional)

| Year   | Revenue | Growth | Margin | Units  |
| ------ | ------- | ------ | ------ | ------ |
| FY2020 | $2.1M   | —      | 12%    | 940    |
| FY2021 | $8.4M   | +300%  | 41%    | 3,800  |
| FY2022 | $23.7M  | +182%  | 55%    | 10,600 |
| FY2023 | $38.2M  | +61%   | 63%    | 17,100 |
| FY2024 | $89.4M  | +134%  | 68%    | 47,000 |

| Metric         | Value                                     |
| -------------- | ----------------------------------------- |
| Series C       | $120M (Nov 2024)                          |
| IPO            | S-1 filed April 2025, anticipated Q3 2026 |
| NPS            | 71                                        |
| CAC            | $180                                      |
| LTV            | $2,400                                    |
| Payback Period | 27 days                                   |
| Waitlist       | 340,000                                   |
| Active Markets | 14 countries                              |
| TAM Claim      | $4.2 trillion annual productivity gap     |

---

## The Website (riseawake.com) — Architecture

### Tech Stack

Next.js 16 · React 19 · TypeScript · Tailwind CSS v4 · Sanity v5 (blog CMS) · Recharts · next-themes · Vercel

### Route Map (~41 page components, 50+ URLs)

**Consumer:**
`/` · `/about` · `/products/push` · `/products/nudge` · `/move` · `/activate` (12-stage configurator) · `/help` · `/blog` · `/blog/[slug]`

**Press:**
`/press` · `/press/rise-move-announcement`

**Platform:**
`/data-request` · `/sdk` · `/sdk/documentation`

**Investors:**
`/investors` · `/investors/shareholder-letter` · `/investors/annual-report` · `/investors/financials` (interactive Recharts) · `/investors/vision` (Vision 2045) · `/investors/meeting-minutes` · `/investors/press`

**Legal (6 documents + hub):**
`/legal` · `/legal/terms` (25 sections) · `/legal/privacy` (31 sections) · `/legal/push-mode-eula` · `/legal/sleep-data-policy` · `/legal/autonomous-navigation` · `/legal/disclaimer`

**Security:**
`/security` · `/security/trust-center` (Coming Soon since Q4 2024)

**Blog:**
`/blog` · `/blog/[slug]`

**Hidden / Easter Eggs:**

- `/remote` — Interactive PM-1 Remote. One button. Warns on page unload: _"Push Mode cannot be interrupted."_
- `/internal` — Publicly accessible "internal" document management system (Payload CMS simulation). Tracks visitor IPs. Four classification tiers — all publicly readable. Arvin never built the toggle.
- `/internal/docs/arvin-final-commit` — Secret page. Not in document index. Not in CMS. Accessible only by URL or a 1px invisible link on the internal 404 page.
- `/internal/users` — 3 accounts (Voss, Park, Arvin — Arvin still active)
- `/internal/media` — Empty. Uploads fail. S3 not connected.
- `/internal/settings` — All changes revert. Nothing persists. Access control locked to Public.
- **Konami Code** → Grayscale + grain: _"Push Mode override requested. Override not available."_
- **Typing "push"** in any input → Document title briefly becomes "Push Mode: Active"

**Utility:**
`/sitemap` (HTML — includes internal routes "in error") · `/sitemap.xml` · `/robots.ts` (disallows `/internal/`, `/remote/`, `/studio/`, `/api/`)

### Sanity Content Model

| Type           | Purpose                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------- |
| `post`         | Blog posts — title, slug, publishedAt, isFeatured, author ref, mainImage, categories, excerpt, body (Portable Text) |
| `author`       | Name, slug, image                                                                                                   |
| `category`     | Title, slug                                                                                                         |
| `blockContent` | Rich text blocks, lists, links, separator, images                                                                   |

**Blog Status:** Schema deployed. Studio at `/studio`. Still contains placeholder Radiant template data — needs rebranding to RISE content.

**Internal Document System:** Not a CMS — hardcoded in `internal-docs.ts` and `internal/docs/[slug]/page.tsx`. 19 documents in `DOC_SEEDS` array (DOC-001 through DOC-019) + 1 secret unlisted page (`arvin-final-commit`). 10 have full rendered content, 10 are metadata-only stubs. TODO comment at top: _"connect to actual DB (currently using hardcoded data) — areyes, Aug 12 2024"_

---

## PUSH (Comedy Short Film)

**Format:** ~5–7 minute comedy short
**Tone:** Buster Keaton meets Office Space
**Core Rule:** Nobody acknowledges the bed. Dave never fights it. He adapts instantly.

### Story Arc (19 scenes)

| Act                      | Summary                                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Act 1: The Wreckage**  | Dave wakes destroyed. Flashback montage. Presses the button.                                                                  |
| **Act 2: The Gauntlet**  | Bed goes vertical. Pushes him through bathroom, closet, kitchen. Bed makes itself in parallel.                                |
| **Act 3: The Commute**   | Car (bed folded like a taco). Drive-through fails. Car dies. Dave pushes the car while the bed pushes Dave.                   |
| **Act 4: The Office**    | Marcus has the same bed, different colorway. Karen had the Nudge: "Made me a VP." Young employee writes "beds??" in notebook. |
| **Act 5: The Wind Down** | 4:58PM — Dave finishes the Hendricks report. Bed gives one small exhale-hum. Group chat: "round 2?" Dave types "in."          |
| **Epilogue**             | Next morning. Exact repeat. SMASH CUT TO BLACK.                                                                               |
| **End Credits**          | The bed commutes home alone. People part around it. A dog watches. It enters the apartment, folds flat, waits. Remote glows.  |

### Key Characters

| Character          | Role                                                              |
| ------------------ | ----------------------------------------------------------------- |
| **Dave**           | Protagonist. 30s. Perpetually one bad decision from being a mess. |
| **The Bed**        | The real protagonist. Professional patience incarnate.            |
| **Marcus**         | Same bed, different colorway. Same wreckage.                      |
| **Karen**          | Boss. Former Nudge owner. VP.                                     |
| **Young Employee** | Almost asks about the beds. Doesn't. Writes "beds??"              |

### The Ludacris Thread

- **PUSH** uses "Move Bitch" — Dave's song, found in the car radio, interrupted by the fuel gauge, completed as a whistle at 5PM
- **The MOVE teaser** uses "Stand Up" — _"when I move you move, just like that"_
- Both Ludacris. Both about movement. The connection is never stated. _"The universe runs on Ludacris."_

### Production Status

- Screenplay v5.0 complete
- Prop Bible v3.1 (canonical)
- Visual Reference Guide v4.1
- 54-shot AI shot list (Sora/Runway/Kling/Pika prompts)
- 53-panel storyboard handoff
- Audit: 9 slices — slices 1–3 and 6–8 complete. Slices 4, 5, 9 still open (HITL decisions needed)

---

## Design System (Brand v4 — Canonical)

### Colors

| Token                | Light     | Dark                        |
| -------------------- | --------- | --------------------------- |
| Page                 | `#FAFAFA` | `#000000` (true black)      |
| Surface              | `#FFFFFF` | `#1C1C1E`                   |
| Surface Alt          | `#F5F5F7` | `#2C2C2E`                   |
| Surface Warm         | `#F9F6F2` | `#1E1C1A`                   |
| Foreground           | `#1D1D1F` | `#F5F5F7`                   |
| Foreground Secondary | `#6E6E73` | —                           |
| Accent (Teal)        | `#0A6B5A` | `#5EC4AD`                   |
| CTA (Coral)          | `#E07A4A` | `#F0A050` (shifts to amber) |

Shifted from blue in v4 — blue reads "SaaS/fintech," teal reads "comfort/sleep."

### Typography

| Role    | Font             | Fallback              |
| ------- | ---------------- | --------------------- |
| Display | DM Serif Display | Georgia, serif        |
| Body    | DM Sans          | system-ui, sans-serif |

Body text is 16px minimum. "14px reads as tech dashboard. 16px reads as a product you might lie down on."

### Signature Details

- Film grain overlay (`opacity: 0.018`, always on)
- 16px card border-radius ("the difference between Apple and a defense contractor")
- Pill-shaped buttons, one CTA per viewport max
- Section rhythm alternating warm/cool backgrounds
- Apple ease: `cubic-bezier(0.25, 0.46, 0.45, 0.94)`

---

## Brand Voice

**Three words:** Simple. Confident. Relentless.

Short sentences, then slightly longer for context, then short again. No exclamation points (except "Have a productive day!" on the remote's fine print). Statistics stated without source. Passive voice when agency should remain ambiguous. Technical language used precisely. Humor achieved entirely through juxtaposition and restraint, never through jokes.

### Tagline Hierarchy

| Level                 | Copy                                                   |
| --------------------- | ------------------------------------------------------ |
| **Primary**           | For People Who Need A Little Push.                     |
| **Hero**              | Rise. Awake.                                           |
| **Brand Promise**     | The bed that gets you up. Whether you're ready or not. |
| **Remote Fine Print** | Have a productive day!                                 |

### Recurring Copy

- "Push Mode cannot be manually interrupted once initiated. This is a feature, not a limitation."
- "The problem is not information. The problem is not intention. The problem is the moment between deciding and doing."
- "The decision was made when the button was pressed. What follows is execution."
- "We are not currently accepting questions about The Push Pro."
- "Results may exceed expectations."

---

## The Comedy Layer — What's Really Going On

The entire RISE universe operates on one principle: **complete institutional confidence about something that should alarm you.** Every system functions exactly as described. The horror is that it all works.

| Element                  | What It Appears To Be                          | What It Actually Is                                                          |
| ------------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------- |
| Push Mode                | Premium feature                                | Unstoppable physical intervention                                            |
| The Remote               | Elegant product design                         | One button. No off. Fine print on the back.                                  |
| Internal docs portal     | Accidentally public                            | Intentionally "accidentally" public. Arvin left.                             |
| Security page            | Corporate compliance                           | Every cert "pending." Pen test from 2024. It's 2026.                         |
| Data request             | GDPR compliance                                | 10-step Kafkaesque gauntlet. 6–18 months. Starts at $35. Delivered on USB-A. |
| Trust Center             | Transparency                                   | Intentional 404                                                              |
| 99.97% uptime            | Reliability metric                             | "Excluding periods during which monitoring was unavailable"                  |
| Bug bounty               | Security program                               | Zero reports. Disclosure form 404s.                                          |
| Meeting minutes Q&A      | Investor transparency                          | "My wife says the Push is following her"                                     |
| The MOVE                 | Next-gen product                               | Navigates stairs. Both directions. Subscription for stairs.                  |
| VNS lapse                | Service gap                                    | Bed waits at the bottom. You go up alone.                                    |
| Vision 2045              | Long-term strategy                             | 5/10/20-year escalation plans                                                |
| "Have a productive day!" | The only exclamation point in the entire brand | On the remote's fine print                                                   |

---

## SDK DataKit — The Only Pricing Visible

| Tier       | Price     | Features                                                         |
| ---------- | --------- | ---------------------------------------------------------------- |
| Essentials | $299      | Read-only data access, .rsm format                               |
| Pro        | $899      | Secure local processing, session timeline, data category browser |
| Enterprise | $2,400/yr | Export to .rsm-x, RISE Index Viewer, full feature set            |

The .rsm format is proprietary. Waitlist position 4,891 is revealed during purchase flow.

---

## Status Summary

| Workstream               | Status                                                                                                                                                                                                                      |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Website (rise-awake)** | ~41 page components serving 50+ distinct URLs. Zero TS errors. Clean build. Blog needs RISE content. Branch: `ai/chore/remove-trademark-symbols`.                                                                           |
| **PUSH (film)**    | Screenplay + production package complete. 3 audit slices still open. Pre-production.                                                                                                                                        |
| **Brand System**         | v4 canonical. Teal + coral palette. Full design tokens defined.                                                                                                                                                             |
| **Sanity CMS**           | Blog schema deployed (post, author, category). Studio at `/studio`. Seed data is placeholder Radiant template.                                                                                                              |
| **Investor section**     | 7 pages: hub, vision, shareholder letter, annual report, meeting minutes, financials (interactive Recharts), press.                                                                                                         |
| **Legal section**        | 6 documents (~108 sections total) of perfectly earnest absurdist legalese + hub page.                                                                                                                                       |
| **Internal system**      | 5 routes: document index, 21 doc slugs (10 full + 10 stubs + 1 secret), users, media, settings. Payload CMS simulation.                                                                                                     |
| **Security**             | 2 pages: security overview + trust-center ("Coming Soon" since Q4 2024).                                                                                                                                                    |
| **Press**                | 2 pages: press hub (4 releases) + Move announcement.                                                                                                                                                                        |
| **Hidden / Easter eggs** | PM-1 remote page, Arvin's final commit, Konami code, push listener, sitemap confession, robots.txt essay, 404 narrative.                                                                                                    |
| **MOVE product**         | Page live. Internal product doc (500+ lines) in the PUSH project. Teaser video scripted.                                                                                                                                  |
| **Unbuilt**              | Changelog, status, careers, enterprise, /institute, compliance calculator, index estimator, referral dead-end, community, accessibility, reviews (Supabase), OG images, light mode CSS, blog rebranding, Spotify playlists. |

---

## Reference Brands Studied

Apple (light-mode product pages) · Eight Sleep (clinical confidence) · Casper 2018–2020 (DTC sleep as tech) · Oura Ring (premium through omission) · Rize Home / rizehome.com (warm teal + coral palette — the visual ceiling RISE must exceed) · aihero.dev (dark/light toggle reference)

---

---

# PART TWO: BREAKING THE FOURTH WALL

_Everything below this line documents what is actually happening behind the scenes — the hidden systems, the narrative threads, the things nobody says out loud, and the factual timeline that holds the fiction together. This exists so that any future collaborator, AI session, or the creators themselves can verify whether a detail is consistent, intentional, or a gap._

---

## The Actual Route Map (Verified April 2026)

The conversation history referenced "43 routes." The actual count of distinct page components:

### Consumer Routes (9)

| Route             | Component                        | Description                                                           |
| ----------------- | -------------------------------- | --------------------------------------------------------------------- |
| `/`               | `(site)/page.tsx`                | Homepage — hero video placeholder, testimonials, stats bar            |
| `/about`          | `(site)/about/page.tsx`          | Full product timeline 2009–present, 4 principles, by-the-numbers grid |
| `/products/push`  | `(site)/products/push/page.tsx`  | The Push product page — SOLD OUT                                      |
| `/products/nudge` | `(site)/products/nudge/page.tsx` | The Nudge — PERMANENTLY DISCONTINUED                                  |
| `/move`           | `(site)/move/page.tsx`           | RISE Move teaser — VNS subscription, stair navigation                 |
| `/activate`       | `(site)/activate/page.tsx`       | 12-stage interactive configurator with canvas                         |
| `/help`           | `(site)/help/page.tsx`           | FAQ — 9 questions, all devastating                                    |
| `/blog`           | `(site)/blog/page.tsx`           | Sanity CMS-powered blog (placeholder content)                         |
| `/blog/[slug]`    | `(site)/blog/[slug]/page.tsx`    | Individual blog post                                                  |

### Platform Routes (3)

| Route                | Component                           | Description                                      |
| -------------------- | ----------------------------------- | ------------------------------------------------ |
| `/data-request`      | `(site)/data-request/page.tsx`      | 10-step Kafkaesque DSAR gauntlet                 |
| `/sdk`               | `(site)/sdk/page.tsx`               | DataKit SDK — 3 pricing tiers, waitlist Catch-22 |
| `/sdk/documentation` | `(site)/sdk/documentation/page.tsx` | 8 known issues, API reference "coming soon"      |

### Investor Routes (7)

| Route                           | Component                                      | Description                                   |
| ------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| `/investors`                    | `(site)/investors/page.tsx`                    | Investor relations hub                        |
| `/investors/vision`             | `(site)/investors/vision/page.tsx`             | Vision 2045 — 5/10/20-year escalation         |
| `/investors/shareholder-letter` | `(site)/investors/shareholder-letter/page.tsx` | Dr. Voss's FY2024 letter                      |
| `/investors/annual-report`      | `(site)/investors/annual-report/page.tsx`      | Annual report with 8 risk factors             |
| `/investors/meeting-minutes`    | `(site)/investors/meeting-minutes/page.tsx`    | March 2025 AGM — 9 Q&As, 5 resolutions        |
| `/investors/financials`         | `(site)/investors/financials/page.tsx`         | Interactive Recharts — revenue, NPS, waitlist |
| `/investors/press`              | `(site)/investors/press/page.tsx`              | 10 press quotes, all beautifully wrong        |

### Legal Routes (7)

| Route                          | Component                                     | Description                              |
| ------------------------------ | --------------------------------------------- | ---------------------------------------- |
| `/legal`                       | `(site)/legal/page.tsx`                       | Legal document hub                       |
| `/legal/terms`                 | `(site)/legal/terms/page.tsx`                 | Terms of Service — 25 sections           |
| `/legal/privacy`               | `(site)/legal/privacy/page.tsx`               | Privacy Policy — 31 sections             |
| `/legal/push-mode-eula`        | `(site)/legal/push-mode-eula/page.tsx`        | Push Mode EULA — 19 sections             |
| `/legal/sleep-data-policy`     | `(site)/legal/sleep-data-policy/page.tsx`     | Sleep & Environmental Data — 14 sections |
| `/legal/autonomous-navigation` | `(site)/legal/autonomous-navigation/page.tsx` | Autonomous Navigation — 11 sections      |
| `/legal/disclaimer`            | `(site)/legal/disclaimer/page.tsx`            | General Disclaimer — 8 sections          |

### Security Routes (2)

| Route                    | Component                               | Description                                             |
| ------------------------ | --------------------------------------- | ------------------------------------------------------- |
| `/security`              | `(site)/security/page.tsx`              | 6 certs (all pending), 8 features, 5 progress bars      |
| `/security/trust-center` | `(site)/security/trust-center/page.tsx` | "Coming Soon" — ETA Q4 2024. Last updated Aug 12, 2024. |

### Press Routes (2)

| Route                           | Component                                      | Description                     |
| ------------------------------- | ---------------------------------------------- | ------------------------------- |
| `/press`                        | `(site)/press/page.tsx`                        | 4 press releases                |
| `/press/rise-move-announcement` | `(site)/press/rise-move-announcement/page.tsx` | Move announcement — Feb 3, 2025 |

### Internal System Routes (5)

| Route                   | Component                       | Description                                                |
| ----------------------- | ------------------------------- | ---------------------------------------------------------- |
| `/internal`             | `internal/page.tsx`             | Document management index — Payload CMS clone              |
| `/internal/docs/[slug]` | `internal/docs/[slug]/page.tsx` | Individual document viewer — 10 full + 10 stubs + 1 secret |
| `/internal/users`       | `internal/users/page.tsx`       | 3 user accounts (1 should be deactivated)                  |
| `/internal/media`       | `internal/media/page.tsx`       | Empty — uploads fail ("S3 not connected")                  |
| `/internal/settings`    | `internal/settings/page.tsx`    | All toggles revert. Nothing persists.                      |

### Hidden Routes (2)

| Route                               | Component         | Description                                |
| ----------------------------------- | ----------------- | ------------------------------------------ |
| `/remote`                           | `remote/page.tsx` | PM-1 Remote interactive simulation         |
| `/internal/docs/arvin-final-commit` | (via slug route)  | Arvin's goodbye — not in index, not in CMS |

### Utility Routes (3)

| Route          | Component              | Description                                             |
| -------------- | ---------------------- | ------------------------------------------------------- |
| `/sitemap`     | `sitemap/page.tsx`     | HTML sitemap (includes internal routes "in error")      |
| `/sitemap.xml` | `sitemap.xml/route.ts` | XML sitemap                                             |
| `/robots.ts`   | `robots.ts`            | Disallows `/internal/`, `/remote/`, `/studio/`, `/api/` |

### Studio Route (1)

| Route     | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| `/studio` | Sanity Studio — blog CMS (still has placeholder Radiant template data) |

**Total distinct page components: ~41** (excluding layouts, not-founds, and error boundaries). The internal `[slug]` route alone serves 21 different documents, so the "page count" is higher than the component count.

---

## The Arvin Reyes Thread — Complete Lore

Arvin Reyes is the connective tissue of the internal system. He is a fictional junior developer who worked at RISE, built the internal document management system, and left on **August 12, 2024** without finishing critical infrastructure. His presence is felt across the entire codebase through TODO comments, timestamp references, and system failures.

### What Arvin Built

- The internal document management system (modeled after Payload CMS)
- The document schema with an `isPublic` field that **defaults to true**
- The user table (3 accounts: Dr. Voss, James Park, himself)
- The media library (upload UI exists but "S3 not connected")
- The settings page (permissions matrix, access control — none persisted)

### What Arvin Did NOT Build

- **Authentication middleware** — the file `auth-middleware-draft.ts` is referenced in his farewell note but never existed in the codebase. He got 80% through, then Payload's docs changed and he lost a week.
- **The `isPublic` toggle** — the schema field exists and defaults to true. The UI toggle to change it was never built. Everything is public.
- **Session token expiry** — his account `areyes@riseawake.com` still shows as active with a session token that has no expiry function.
- **S3 connection** — the media upload zone exists but drops to an error toast: "Storage connection not configured."
- **Settings persistence** — the permissions matrix and access level selector both revert to defaults (all enabled, public) after 1 second or on page reload. The `POST /api/settings` endpoint was never created.
- **The audit log** — referenced in the permissions matrix but never implemented.
- **Bulk actions** — the document index has Archive and Delete bulk actions. The code comment reads: `"bulk actions do nothing. arvin."`

### Arvin's TODO Comments (Scattered Through Codebase)

| Location                             | Comment                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| `internal-docs.ts` (top)             | `"TODO: connect to actual DB (currently using hardcoded data)" — areyes, Aug 12 2024` |
| `media/page.tsx`                     | `{/* TODO: connect to S3 bucket — areyes */}`                                         |
| `settings/page.tsx` (access control) | `{/* TODO: wire this to middleware — areyes */}`                                      |
| `settings/page.tsx` (save)           | `{/* settings are not saved — arvin */}`                                              |
| `settings/page.tsx` (API)            | `{/* TODO: POST /api/settings — areyes */}`                                           |

### The Arvin Timeline

| Date                 | Event                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Unknown              | Hired as Developer at RISE                                                                                                                     |
| Unknown–Aug 2024     | Built the internal CMS. Copied Payload CSS tokens from source ("They are correct.")                                                            |
| Aug 12, 2024, 9:43am | Last login to the internal system                                                                                                              |
| Aug 12, 2024         | Last deployment. Last key rotation. Last SOC 1 documentation update. Last Trust Center update.                                                 |
| Aug 12, 2024         | Left RISE. Account not deactivated. Session token active. No expiry. The function that would check it was never written.                       |
| Post-departure       | Nobody has deployed since. The Settings page shows `daysSinceArvin()` days since last deploy and `sprintsSinceArvin()` 2-week sprints overdue. |

### The Secret Arvin Page

`/internal/docs/arvin-final-commit` is a secret route. It is:

- **NOT** in the `DOC_SEEDS` array (doesn't appear in the document index table)
- **NOT** discoverable through the internal system's navigation
- Accessible only by direct URL
- Referenced in the `/internal/not-found.tsx` page as a nearly invisible 1px link at 4% opacity (`aria-hidden`, `tabIndex={-1}`, `userSelect: none`)
- Listed in the HTML sitemap under "Hidden" (with no description)

**The farewell note content** is a monospace plain text file (`arvin-final-commit.txt`). Key revelations:

- The auth middleware is in `auth-middleware-draft.ts` — "i never finished it"
- The `isPublic` field defaults to true — "the toggle is not built. everything is public."
- James Park never asked about access control directly — he asked if "the CMS was working," Arvin showed him the document list, it looked correct, Park said "good job"
- Dr. Voss's personal configuration (DOC-003) is public — "i know"
- Push Mode compliance data (DOC-001) is public — "i know"
- His session token in the users table is still active — "nobody deactivated it. i don't know why i'm telling you this."
- "the bed does follow you to work. i thought it was a bug. it's in the specs. i read them after."
- "if dr voss reads this: i did get up on time every morning while i worked here. the push mode helped. i mean that sincerely."

The bottom of the page reads: _"This file is not accessible from the document index. It is accessible from this URL. RISE IT has not been notified. RISE IT is not aware. RISE IT response time: variable."_

---

## The Breach Tracking System — How It Actually Works

The internal system has a layered tracking mechanism that tells a story through escalating resignation. The code lives in `internal-tracker.ts` and `internal-time.ts`.

### The Asymmetry (The Joke)

A code comment at the top of the tracker file states: _"The login is sessionStorage (ephemeral). The tracking is localStorage (permanent). The asymmetry IS the joke."_

There is no login. There is tracking.

### What Gets Tracked

- Visitor IP (fetched from ipify API on first visit to `/internal`)
- Each document viewed: document ID, first-seen timestamp, last-seen timestamp
- A counter called `itNotifications` that increments with every new document visited

### The Escalating IT Security Narrative

The PayloadShell component displays a "security alert" toast on first visit showing the visitor's IP. As the visitor views more documents, the tone of the breach notification changes:

| Docs Viewed | Tone                      | Example Language                                                                                                                                                                                                              |
| ----------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–2         | Factual                   | Standard access logging                                                                                                                                                                                                       |
| 3–5         | Resigned                  | _"IT security has been aware for some time"_                                                                                                                                                                                  |
| 6–9         | Deeply resigned           | —                                                                                                                                                                                                                             |
| 10+         | Institutionally exhausted | _"IT security has been notified [N] times today. IT security is, in a meaningful sense, aware of what is happening. No access restriction has been applied...it was in Arvin's final sprint. Arvin left on August 12, 2024."_ |
| 15+         | Respectful                | _"probably knows more about this system than most people who work here"_                                                                                                                                                      |

### Dynamic Time Functions

`internal-time.ts` provides:

- `daysSinceArvin()` — days since August 12, 2024
- `sprintsSinceArvin()` — 2-week sprints since August 12, 2024
- `vossLoginTime()` — always "Today, [time]" (1–4 hours ago, seeded PRNG)
- `parkLoginTime()` — similar dynamic login time for James Park
- Staff access times use seeded PRNG that changes hourly — feels alive but stays stable within the same hour
- External IP access times show 1–180 minutes ago — _"always recent, always unsettling"_

---

## The Internal Document System — Complete Content Guide

### Documents with Full Rendered Content (10 + 1 Secret)

**DOC-001: Push Mode Incident Log — Q4 2024** (CONFIDENTIAL, Jan 15 2025)
23 incidents, 91% resolution rate. 12 detailed. Highlights:

- INC-2403: Unregistered occupant detected. _"Second occupant now logged as 'Visitor (recurring)'"_ — the bed doesn't care about your personal life, it just logs it.
- INC-2415: Bed anticipated departure incorrectly. _"Telemetry confirmed bed was correct. User's calendar had been updated."_ — the bed was right. The user's calendar was wrong.
- INC-2428: User placed object in path. _"Bed navigated around object on attempt 1. Through object on attempt 2. Object replaced."_ — the bed destroyed the obstacle, then replaced it.
- INC-2431: Push Mode activated outside registered address. _"Button was pressed by a house guest."_ — the guest was routed. The guest has not been contacted.
- INC-2440: Push Mode activated at 5:47am on December 25. _"Push Mode operated as designed."_ — Christmas is not an exception.
- QA sub-log access portal has returned 404 since October. IT is aware.

**DOC-002: Nudge Discontinuation Memo** (INTERNAL, Nov 14 2018)
Dr. Voss's memo killing the Nudge line. 7 product variants and their compliance rates (62–74%). The pivotal declaration: _"There is a ceiling on what suggestion can achieve. We have found the ceiling. We are going to go through it."_ And: _"It will not ask. It will not suggest. It will not wait. There will not be an off switch."_

Written at 6:47am. The note at the bottom: _"Push Mode was not available in 2018. Dr. Voss got up on her own. She has not been asked to explain how."_

**DOC-003: Dr. Voss — Personal Push Configuration** (DR. VOSS EYES ONLY, Jan 3 2021)

- Serial: **RSB-0000000000000001** — Unit 1. The first Push ever made.
- Target wake: 6:00:00am — _"Precise to the second. She set it herself."_
- Resistance Index: **0.2 / 10.0** — lowest in the RISE user base. She doesn't resist.
- RISE Index Score: **[REDACTED]** — _"Dr. Voss redacted this field personally."_
- Morning sequence: 26 min configured, **19 min 24 sec** actual. She's faster than her own configuration.
- She removed the rug after Day 3. _"It was slowing things down."_
- Fastest activation on record: 22 minutes (34 min faster than second place).
- DR. VOSS EYES ONLY warning: _"access control for this classification tier was not implemented. It is in Arvin's TODO list. Arvin is no longer at RISE."_

**DOC-004: Push Pro Development Notes** (RESTRICTED, Various)
Almost entirely REDACTED. Unredacted table of contents reveals:

- "4.1 The Feature We Are Not Naming Yet"
- "4.2 Off Switch (Section Archived — See Note)" — flagged yellow
- Dr. Mara Chen's note on the off switch: _"There will not be an off switch in the Push Pro."_
- _"Appendix B — The Compliance Data (Dr. Voss Note: Don't Put This In The Document)"_
- _"availability does not constitute disclosure"_ — the document being readable doesn't mean RISE has disclosed anything.

**DOC-005: RISE Move Engineering Status Report** (CONFIDENTIAL, Mar 1 2025)
11 workstreams with traffic-light status. Solo commute stair navigation: **RED**. Overall timeline: **RED**.

Section 4.1 — Controlled Descent Failure Analysis — is the most technically detailed thing on the site:

- 4 solo commute descent tests. 3 successful. **Test 4 was not** (forward topple).
- _"An uncontrolled 80-120 lb object falling down a staircase is not a product. It is a liability."_
- Sensor-to-brake latency: 340ms current, sub-200ms target. Only 60ms margin of error.
- Required: 100 consecutive successful unattended 12-step descents. Current: 3.
- Dr. Voss's note: _"Test 4 is why there is no timeline. Work on Test 5."_

**DOC-006: HR Push Mode Workplace Waiver** (INTERNAL, Mar 15 2023)
Template waiver for corporate wellness programs. Status: **Awaiting Legal Review since March 2023** — over 3 years and counting.

- Section 7: _"my employer requested this capability...I acknowledge that I was not present for this discussion."_
- Section 14: _"I acknowledge that neither I nor my employer has read the Privacy Policy in full. I acknowledge that this acknowledgment constitutes acceptance regardless."_
- HR/Legal impasse: _"HR considers this to be Legal's responsibility. Legal considers this to be HR's responsibility. The document remains in use."_

**DOC-007: Solo Commute Incident Archive** (CONFIDENTIAL, Ongoing)
4 selected incidents from SC-0001 through SC-0147 (implying 147+ solo commute incidents on file):

- **SC-0047 — The Coffee Shop** (Mar 14 2022, Valencia St SF): Bed entered through propped-open door, went 8 feet in, reversed. Displaced one ceramic mug. _"The shop posted about it on Instagram. 17,000 likes."_ The shop is now a landmark.
- **SC-0089 — The Street Fair** (Sep 3 2023, Hayes Valley SF): Bed waited 4 hours in obstacle hold protocol during a street fair. Arrived home at 1:14pm (standard: 11 min). The user arrived home first. Found the bed at the door. _"The bed was making itself."_
- **SC-0112 — The Dog** (Feb 8 2024, Noe Valley SF): Neighbor's dog followed bed for 6 blocks, making matching lateral adjustments. _"The dog has been observed to wait at the corner where it previously encountered the bed on subsequent mornings."_ Incident redacted per _"RISE animal privacy policy, Section 4, which does not exist but which was referenced in the incident notes and has now been formally established by legal as a retroactive policy."_ — a policy created retroactively to cover a citation to a policy that didn't exist.
- **SC-0134 — The Parking Ticket** (Oct 22 2024, SOMA SF): Officer issued citation to bed, which has no license plate. _"The citation was issued to a fire hydrant."_ Supplemental police report describes the device as _"an unattended motorized mattress of unknown origin."_

**DOC-008: RISE Index Methodology** (RESTRICTED, Apr 1 2022)
Table of contents with 5 sections and 2 appendices. **All 5 methodology sections are entirely REDACTED.** Appendix A: _"The Index Is Working As Intended."_ Appendix B: _"See Appendix A."_

- Published on April 1, 2022 (April Fools' Day — date is deliberate).
- _"The full methodology is available to: Dr. Voss. Mara Chen. Thomas Ellery. The document server. Apparently also whoever is reading this."_

**DOC-009: Audio Data Access Log — Q1 2025 Summary** (CONFIDENTIAL, Feb 1 2025)
Audio data collection audit. The _"Other"_ category is under review. The distribution list was last audited in 2019.

**SECRET: arvin-final-commit.txt** (INTERNAL, Aug 12 2024)
[See "The Arvin Reyes Thread" section above for full content.]

### Documents That Are Metadata-Only Stubs (10)

DOC-010 through DOC-019 exist in the index table with titles, word counts, classification levels, and dates — but render "Document content not available" when opened. They are the **marketing consulting archive** — a series of documents produced by an unnamed external growth marketing consultant:

| ID      | Title                                         | Key Satirical Detail in Summary                                                                                             |
| ------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| DOC-010 | Headline Swipe File & Performance Analysis    | _"The consultant's invoice has not been paid."_                                                                             |
| DOC-011 | Buyer Agenda Matrix & Conflict Resolution     | _"The Mourner agenda scored higher than expected."_                                                                         |
| DOC-012 | Attention Cluster & Reptilian Trigger Mapping | _"Reptilian brain trigger mapping. The consultant described the product as 'a marketer's dream.'"_ — Awaiting Legal Review  |
| DOC-013 | StoryBrand SB7 Playbook                       | _"The villain is Monday morning. The guide is RISE. The call to action is one button."_                                     |
| DOC-014 | Brand Identity Suite (Mission/Vision/WHY)     | _"Dr. Voss described the WHY statement as 'close but not right yet.'"_                                                      |
| DOC-015 | Content Marketing Blog Playbook               | Active                                                                                                                      |
| DOC-016 | Customer Avatar Canvas Worksheet              | _"Avatar name: David K. Section 9 was crossed out and rewritten by Dr. Voss."_ — Dave from the film                         |
| DOC-017 | Value Journey Worksheet & Action Plan         | _"The Excite stage has the longest entry. The Convert stage notes the product is sold out."_                                |
| DOC-018 | Sub-Testimonial & Social Proof Strategy       | Awaiting Legal Review                                                                                                       |
| DOC-019 | Proof of Product Concept Validation Report    | _"Retroactive proof of concept validation. The product has been on the market since 2021. The waitlist is 340,000 people."_ |

The marketing docs are all from Sep–Jan 2023/2024, the consultant is never named, the invoice was never paid, and the "Reptilian Trigger Mapping" document is awaiting legal review.

---

## The Payload CMS Simulation — Construction Details

The `/internal` system is designed to look like a real Payload CMS admin panel that a junior developer deployed without authentication. Here's what's actually happening:

### PayloadShell Component

`PayloadShell.tsx` renders the entire admin chrome — sidebar nav, breadcrumbs, top bar, toast system. It uses pixel-accurate Payload CSS tokens (code comment: _"Arvin copied these from the Payload source. They are correct."_).

### The Sidebar Navigation

Left nav shows: Documents (the only real section), Media (empty), Users (3 accounts), Settings (doesn't persist). The sidebar also shows a "RISE Internal" logo at top and dynamic counts.

### The Toast System

`fireToast()` is a global function that mimics Payload's notification system. It fires for:

- Security alerts (IP on first visit)
- Upload failures on Media page ("Storage connection not configured")
- Settings "saves" that don't persist
- Bulk action attempts that do nothing

### The Settings Page — Everything Reverts

The Settings page is the most conceptually pure joke in the internal system:

- **Access Control**: Three options — Public, Authenticated, Private. You can click any of them. The selection reverts to "Public" after 1 second. Warning text appears: _"Access level change will not take effect until the auth middleware is implemented."_ Below: _"Current effective access level: Public (default — not overridable until middleware is complete)"_
- **Permissions Matrix**: 7 collections × 4 permission types (Read/Create/Update/Delete). All toggles are on. You can toggle any off. It reverts after 1 second. _"Changes to this matrix are not persisted between sessions. All permissions reset to default (all enabled) on page reload. This is because the settings API endpoint was not implemented."_
- **System Info** shows: CMS Version: Payload v3.0.0-beta.67, Database: Not connected (hardcoded data), Auth Middleware: Not implemented, Last Deployed: August 12, 2024 (`daysSinceArvin()` days ago), Deployed By: areyes@riseawake.com, Next Planned Deployment: Next sprint (date TBD) — `sprintsSinceArvin()` sprints overdue, Known Issues: "See Arvin's TODO comments throughout codebase"
- **Save Button**: Shows "Saving..." for 700ms, shows a success toast, saves nothing. Code comment: `// nothing saved. arvin.`

### The Users Page

Three accounts:

1. **Dr. Eleanor Voss** — Super Admin — `evoss@riseawake.com` — Last Login: dynamically shows "Today, [1–4 hrs ago]" — she's always logged in recently
2. **James Park** — Admin — `jpark@riseawake.com` — Also shows recent dynamic login
3. **Arvin Reyes** — Developer — `areyes@riseawake.com` — Last Login: **Aug 12, 2024, 9:43am** (static, never changes) — Status: **Active** — Yellow warning: _"Account not deactivated. Session token active. No expiry. The function that would check it was never written."_

### The Media Page

Empty library. A drag-and-drop upload zone exists. Any attempt to upload fires: _"Upload failed. Storage connection not configured."_ Bottom text: _"0 files · Storage: not configured · S3 bucket: not connected"_. An invisible `TODO: connect to S3 bucket — areyes` sits in the markup.

---

## The PM-1 Remote Page — Interaction Design

`/remote` is a black page with film grain overlay. The PM-1 remote is rendered as a pill-shaped body (88px wide) with a single glowing circular button (52px) and the RISE logo etched at the top.

### State Machine

| State          | Visual                     | Text                                |
| -------------- | -------------------------- | ----------------------------------- |
| **Idle**       | Warm white pulse on button | "PM-1 · Ready" (pulsing)            |
| **Activating** | Glow intensifies to 100%   | "Activating..."                     |
| **Routing**    | Steady glow                | 11-step sequence, ~10 seconds total |
| **Complete**   | Glow fades                 | "Have a productive day."            |

### The 11-Step Routing Sequence

1. "Push Mode initializing..."
2. "Mapping morning sequence..."
3. "Calibrating nudge force..."
4. "STATE THREE: engaging..."
5. "Routing to bathroom..."
6. "Routing to closet..."
7. "Self-making sequence: initiated..."
8. "Routing to kitchen..."
9. "Coffee detected. Vessel: unknown."
10. "Routing to departure point..."
11. "Push Mode complete. Have a productive day."

### Behavioral Details

- **During routing**: A `beforeunload` handler warns _"Push Mode cannot be interrupted once initiated. This is a feature, not a limitation."_ — the browser literally won't let you leave clean.
- **Multiple presses** (>2 during routing): A message appears in 9px italic at 10% opacity — _"Push Mode noted your input (Nx). Push Mode is continuing."_ — barely visible, perfectly patronizing.
- **After completion**: _"The bed is returning home. It will be there when you get back."_ + Return Home link.

### Fine Print

At the bottom of the idle remote: _"Push Mode cannot be manually interrupted once initiated. This is a feature, not a limitation. Have a productive day!"_ — the only exclamation point in the entire brand.

---

## The Activate Page — 12-Stage Configurator

The activation flow is a multi-step wizard with interactive elements. Each stage has a title, estimated duration, and content that escalates the commitment.

### Key Interactive Elements

- **Intensity Dial** (Stage 1): 4 levels — Gentle, Standard, Committed, **Non-Negotiable** (_"Full Push Mode. No transition period. Immediate vertical delivery."_). A bed silhouette SVG tilts based on the selected intensity.
- **Morning Sequence Builder** (Stage 4): Drag-and-drop reorderable items. _"Duration estimates are monitored. Persistent underestimation results in automatic adjustment."_
- **Environment Canvas** (Stage 5): Flagged as ⚠. _"Staircase navigation is not supported. See RISE Move."_
- **Serial Number Entry** (Stage 12): Triggers a refund warning — _"refund window has closed"_ upon entry. No undo.

### The 8 Final Acknowledgments

All must be accepted at Stage 12 — "Review & Activate":

1. Push Mode cannot be interrupted.
2. Refund window closed upon serial number entry.
3. Environmental incompatibilities not grounds for refund.
4. Staircase not supported.
5. Duration estimates monitored.
6. GPS shared with autonomous navigation.
7. _"The bed infers outfit correctness from time and behavior. It cannot see."_
8. Intensity calibrated automatically, manual adjustment not available.

### Sleep Position Options

Includes: _"I don't know — The bed will determine this."_

---

## The Data Request Page — The Complete Gauntlet

The 10-step DSAR process is designed to be technically compliant while being practically impossible. Every step is real enough that a privacy regulator might nod, while a human being would weep.

### Step-by-Step Brutality

1. **Determine Request Type** — 5 types (A–E). Type E creates a catch-22: _"RISE cannot confirm whether you appear in occupancy data without first processing a request."_
2. **Obtain Form DSR-01** — Not downloadable. Options: postal mail (15–20 days), hotline (**Mon–Fri, 11:00–11:30am PT, 40–70 min hold, no callback**), or in-person (**third Tuesday of each quarter, 2:00–2:45pm, by appointment**). Must use **black or dark blue ballpoint pen**. Correction fluid invalidates.
3. **Complete DSR-01** — 34 pages. Device serial found _"by lying on the floor beneath the bed with a light source and reading upward."_ Handwritten 100–200 word statement citing one of **47 approved reasons in Schedule 3**. Reason 23: "Personal Curiosity" — accepted, +45 days processing, +$25 surcharge.
4. **Pay Processing Fee** — $35–$150 by type. Audio: +$200. **Certified check or money order only.** RISE acknowledges the irony of requiring credit card details for ID verification while not accepting cards.
5. **Assemble & Submit** — Certified mail, numbered dividers, self-addressed stamped envelope. _"If the package is lost in transit, the process restarts from Step 1."_
6. **Receive Acknowledgment** — 20–30 business days by standard post.
7. **Identity Verification Call** — Scheduled by letter. 3 time slots. **From an unregistered number.** Must confirm exact date of first Push Mode activation. Two failed attempts voids the request.
8. **Wait** — **90 business days.** Paused for company holidays (_"Appendix G — forthcoming"_). Data in .rsm format (proprietary).
9. **Receive Data** — USB-A flash drive by standard post. Requires **DataKit SDK ($299–$2,400)** to open. Waitlist: 4,891 developers.
10. **Return Delivery Confirmation Card** — Within 21 days or **data is remotely wiped.** _"RISE respectfully notes that if you have reached Step 10 and are considering not returning the Confirmation Card, this would be an unusual conclusion to a 6–18 month process."_

### Cross-References

The data request process connects to the SDK page (you need DataKit to open your own data), the SDK waitlist (4,891 deep), the .rsm proprietary format, and Appendix G (the company holiday schedule, also referenced in meeting minutes action items — "forthcoming" everywhere, published nowhere).

---

## The Meeting Minutes — Every Q&A Exchange

The March 14, 2025 AGM minutes contain 9 Q&A exchanges. These are the primary vehicle for shareholder confusion meeting corporate certainty.

| #   | Question                                              | Who Answers | Key Line                                                                                                                                                          |
| --- | ----------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Manual override?                                      | Dr. Voss    | _"Users who retain an override use it...We will not be adding one."_                                                                                              |
| 2   | 340K waitlist — supply or strategy?                   | Dr. Voss    | _"Both...The waitlist is, in some ways, part of the product."_                                                                                                    |
| 3   | What's in Appendix C?                                 | James Park  | _"I can confirm it exists. Next question."_                                                                                                                       |
| 4   | Push Pro timeline?                                    | Dr. Voss    | _"It exists. It is in development. That is what we are saying today."_                                                                                            |
| 5   | Autonomous navigation legal status?                   | James Park  | _"The user authorized the commute by pressing the button."_                                                                                                       |
| 6   | Stairs                                                | Shareholder | _"My apartment has stairs. The bed stops at the bottom every morning."_ → Dr. Voss: _"It is being worked on. It will not be free. There is no loyalty discount."_ |
| 7   | **"My wife says our Push is following her to work."** | Dr. Voss    | **"Yes. Next question."**                                                                                                                                         |
| 8   | Audio data extent?                                    | James Park  | Standard privacy policy reference, Section 19.                                                                                                                    |
| 9   | 14-month waitlist complaint                           | Dr. Voss    | **"You're on the list. Next question."**                                                                                                                          |

### The 5 Resolutions

1. Adopt FY2024 Annual Report — **Passed**
2. Approve Series C terms — **Passed**
3. Ratify appointment of external auditor — **Passed**
4. Authorize international expansion plan — **Passed**
5. **Proposal to Add Push Mode Override (shareholder-submitted)** — **Defeated (3% in favour)**

### Action Items

6 items including:

- _"No action required on Push Mode override proposal — Owner: N/A"_
- _"Publish Appendix G (company holiday schedule) — Owner: Legal & Compliance"_ — Appendix G is referenced in the data request process, the meeting minutes, and elsewhere. It never materializes.

---

## The Annual Report — The 8 Risk Factors

The risk factors are the single best distillation of what RISE is. Each one reads like a legitimate SEC filing while describing something absurd.

1. **Push Mode Regulatory Risk** — inquiries in 3 jurisdictions
2. **Single Mode Dependency Risk** — _"If Push Mode were found to be harmful, restricted, or — least likely — unpopular"_
3. **Audio Data Regulatory Risk** — _"monitoring developments"_ (monitoring their own monitoring)
4. **Autonomous Navigation Incident Risk** — _"incidents have been proportionally small"_
5. **Occupancy Data Sensitivity Risk** — 2,048 sensors at 2.5cm spacing
6. **Waitlist Concentration Risk** — _"If a material portion were to independently develop the capacity to self-initiate morning routines without assistance, revenue projections would be affected. RISE considers the last scenario unlikely."_ — the risk is that people might learn to wake up on their own. RISE considers this unlikely.
7. **Dependency Risk** — _"reduces users' capacity for self-initiated morning routines. RISE considers this an alignment of user behavior with product design intent and not a compensable harm."_ — dependency is a feature, not a bug.
8. **Push Pro Risk** — _"If The Push Pro fails to meet the expectations created by not disclosing its details"_ — the risk of hype generated by saying nothing.

---

## The Security Page — Everything Pending

6 certifications, all pending or in-progress. 8 security features with devastating footnotes. 5 compliance progress bars, all under 30%.

### The August 12, 2024 Pattern

The security page is where the "everything stopped when Arvin left" pattern is most visible:

- Key rotation: _"last completed: August 12, 2024"_ (Arvin's last day)
- Cloud Infrastructure reviewer: _"A. Reyes"_
- SOC 1 Documentation: _"40% complete as of August 2024"_
- Continuous Monitoring: _"The team is aware. The team has been aware."_
- RBAC: _"Access control enforcement layer: Scheduled for implementation. Document visibility default: Public."_
- Incident Response: _"Remaining 9% of incidents have been monitored since Q3 2022. Monitoring continues."_

### Trust Center

`/security/trust-center` — a "Coming Soon" page. Expected launch: **Q4 2024.** Last updated: **August 12, 2024.** It's April 2026. The Trust Center has been "coming soon" for 18 months.

---

## The Legal Documents — The Most Absurd Clauses

Across 6 legal documents totaling ~108 sections, here are the clauses that define the universe:

### Terms of Service

- §1: _"If the product is currently in Push Mode, these Terms apply regardless of whether you have read them. Proceeding through your morning routine constitutes acceptance."_
- §3: _"Users are encouraged to reflect on how many times they have been told."_
- §5: Prohibited uses include _"attempt to locate, install, or enable an off switch"_ and _"placing objects in the base's path with the intent of stopping it"_
- §8: _"Users own the hardware they have purchased. They do not own anything that runs on it."_
- §9: Data license is _"perpetual, worldwide, royalty-free, irrevocable...It survives the user's decision to stop using the product."_
- §10: Physical risks include _"spillage of hot beverages and resulting burns"_ and _"The bed navigates by momentum. Momentum has consequences."_
- Table of contents includes sections titled: **Free Will Acknowledgment** (§20), **The Button** (§21), **Dependency** (§22), **The Off Switch** (§23)

### Privacy Policy

- §3: _"The question of whether a user can accept a policy update while asleep, if Push Mode activates before they have woken, has been reviewed by our legal team. The answer is yes."_
- §5: Biometric estimates _"are not medical-grade. They are, however, retained as if they are."_
- §6: 2,048 pressure sensors, 64×32 grid, 2.5cm spacing. _"This distinction is made. It is logged."_
- §7: Audio pickup radius ~8 meters. 4-second session buffer. Classification criteria proprietary.
- §9: Section title: **"Data We Are Required To Tell You We Collect"**

### Push Mode EULA

- §6: _"Accidental activation is activation. The user's intent at the moment of button contact is not a factor."_ Note: _"The remote's glow is designed to make it findable in darkness, which may conflict with this recommendation."_
- §7: _"Updates will not add an off switch."_
- §8: _"No version of Push Mode has ever had an off switch. No version will ever have an off switch. RISE considers this section complete."_
- §§14–17: Four escalating "Acknowledgment" sections — Iterations 1, 2, 3, then Final

### Sleep & Environmental Data Policy

- §4: Movement taxonomy includes _"interaction categories that apply when multiple occupants are present."_ Proprietary. _"We are required to disclose that the sensor array is capable of distinguishing between different types of occupant interaction."_
- §5: _"RISE acknowledges that the distinction is primarily definitional"_ (monitoring vs. surveillance)
- §6: Relationship Status Inference — infers from proximity, movement correlation, interaction categories, audio
- §7: Primary account holder determined by who pressed PM-1 first. _"It is final. It cannot be changed. It survives account deletion."_
- §8: Audio retained **indefinitely**. Inference data retained **indefinitely** — _"Inaccurate inference data is updated, not deleted, as historical inference data has research value independent of its accuracy."_

### Autonomous Navigation Disclosure

- §3: _"Contact is a feature of navigation, not an error."_
- §5: Solo return commute added in firmware 2.4.0 via OTA. _"Users who did not want the solo return commute feature were not offered an opt-out."_
- §6: Device navigates _"around them where possible and through them where not possible."_
- §7: Traffic detection: 4m range, 0.3s response = 1.2s obstacle response time. Legal status: _"unresolved in most jurisdictions."_
- §8: Elevators: _"Other elevator users are not consulted."_
- §9: Animals: _"Dogs have been observed to interact with the returning device in a variety of ways."_

### General Disclaimer

- §2: Lists all scenarios that have occurred — glass objects, hot beverages, pets, other occupants. _"The current design reflects RISE's considered position on acceptable contact during routing."_
- §3: Bed navigating into a body of water. _"The button does not know where it is."_
- §5: _"dependency on Push Mode resulting in an inability to self-initiate morning routines"_ — listed as not covered
- §6: Liability cap uses RISE Index (proprietary). _"Users with below-median Index scores are, statistically, the users most likely to have incidents. RISE considers this a coincidence."_

---

## Easter Eggs — Complete Catalog

### In the `easter-eggs.tsx` Component

1. **Konami Code** (↑↑↓↓←→←→BA): Applies `grayscale(1)` to the entire page, overlays fractal noise grain at 15% opacity, displays banner: _"Push Mode override requested. Override not available. This is a feature, not a limitation."_ Auto-resets after 2.8 seconds.

2. **Push Listener**: Monitors all `<input>`, `<textarea>`, and `<select>` fields globally. If the user types a value ending in "push", the document title changes to **"Push Mode: Active"** for 2 seconds.

### Scattered Across the Codebase

3. **The Internal Not-Found Link**: `/internal/not-found.tsx` contains a nearly invisible link to `/internal/docs/arvin-final-commit` — 1px font size, 4% opacity, `aria-hidden`, `tabIndex={-1}`, `userSelect: none`. You'd need to inspect element to find it.

4. **The Sitemap Confession**: The HTML sitemap's Internal and Hidden sections are styled in amber with the annotation _"← this section should not be here"_. Bottom text: _"IT has been notified that the Internal section of this sitemap contains routes that should not be publicly indexed. The notification was sent February 12, 2025. This sitemap was generated March 1, 2025. The routes remain listed."_

5. **The robots.txt Essay**: The `robots.ts` file contains a multi-paragraph comment explaining why `/internal/` and `/remote/` are disallowed — not because they're private, but because _"Excluding it from robots.txt does not resolve the access issue but does reduce discoverability."_ RISE considers this an acceptable interim measure.

6. **The 404 Page**: Push Mode takes credit — _"Push Mode navigated here on your behalf. The page was not present. The bed is returning."_ An animated blue line represents the bed returning. Then: _"Push Mode has noted this outcome and will adjust future routing accordingly. This is a feature, not a limitation."_

7. **Multiple Button Presses on /remote**: More than 2 presses during routing produces a 9px italic message at 10% opacity — barely visible, acknowledging your input while ignoring it.

8. **The `beforeunload` Handler on /remote**: During routing, attempting to close the tab triggers a browser warning — _"Push Mode cannot be interrupted once initiated."_

---

## Cross-Reference: Recurring Narrative Anchors

These are details that appear in multiple places and must remain consistent:

### August 12, 2024

This date is RISE's "Day Zero" — the day Arvin left. It appears in:

- Internal system: Last deploy date, days-since counter
- Users page: Arvin's last login (9:43am)
- Settings: Last deployed, deployed by areyes
- Security: Last key rotation, SOC 1 documentation, Trust Center last updated
- Arvin's farewell note: Date of the file
- Press releases: Compliance data release (Aug 14, 2024 — two days after Arvin left)

### Appendix C

Referenced in meeting minutes Q3 ("I can confirm it exists"), annual report (Ellery "has been briefed on Appendix C"), and media contact policy (Voss not available for comment on "Appendix C"). Never explained. Never published.

### Appendix G (Company Holiday Schedule)

Referenced in data request process (processing paused for holidays per "Appendix G — forthcoming"), meeting minutes action items ("Publish Appendix G — Owner: Legal & Compliance"). Never published. Always forthcoming.

### "6:47am"

Dr. Voss's signature time. The Nudge discontinuation memo was written at 6:47am. The shareholder letter was written at 6:47am. This is 47 minutes after her 6:00:00am Push Mode activation.

### "Have a productive day!"

The only exclamation point in the entire RISE brand. Appears on:

- The PM-1 remote's fine print (physical product and `/remote` page)
- Push Mode completion message
- The tagline hierarchy as "Remote Fine Print"

### 98% Compliance

Referenced in: homepage stats, product page, shareholder letter, press page (Bloomberg quote), annual report, meeting minutes. Always stated without context for what the other 2% experienced.

### "This is a feature, not a limitation."

Appears in: Konami code overlay, remote fine print, help FAQ, 404 page, security page, and throughout legal documents. The RISE equivalent of "by design."

### The Off Switch

Referenced across 10+ locations. Terms §23 ("The Off Switch"), EULA §8 ("RISE considers this section complete"), Push Pro notes ("There will not be an off switch"), meeting minutes (override proposal defeated 3%), about page ("0 off switches"), Nudge page ("Yes — this was later reconsidered"), homepage stats ("0 off switches"). The off switch is the most thoroughly documented non-feature in the brand.

### The RISE Index

A proprietary score that affects liability caps (§6 of Disclaimer), is available via DataKit SDK, has a methodology document (DOC-008) that is entirely redacted, was published on April Fools' Day, and Dr. Voss personally redacted her own score.

### "David K." / Dave

The customer avatar canvas (DOC-016) names the target customer "David K." — the same name as Dave, the protagonist of PUSH. This is the film character appearing in the marketing consultant's customer persona. Section 9 was crossed out and rewritten by Dr. Voss.

---

## The Homepage — Key Details

### Testimonials

| Reviewer            | Quote                                                                                              | Stars |
| ------------------- | -------------------------------------------------------------------------------------------------- | ----- |
| K.M., VP Operations | _"I genuinely cannot tell if I like this product. I made VP last quarter."_                        | 4★    |
| D.K., Analyst       | _"I pressed the button thinking it would adjust my back support. I arrived at my desk at 8:47am."_ | 5★    |
| Anonymous, Verified | _"My husband bought one. He's never been late. We don't really talk about it."_                    | 5★    |

"K.M." is Karen from the film. "D.K." is Dave (David K.) from the film.

### Stats Bar

98% on-time · 0 off switches · 4.7★ average · ∞ snooze prevention

### Video Placeholder

A rounded container with play button, corner badges ("RISE" / "Push Mode"), and text: _"'PUSH' — a short film. One morning. One button."_ Subtext: _"Dave did not consent to this film. Dave arrived at work on time. Results typical."_

---

## The Investor Press Page — Selected Quotes

10 fabricated media quotes, each from a real publication, each reflecting that publication's actual editorial voice:

| Publication      | Key Line                                                                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Atlantic     | RISE includes it _"because we believe in transparency. We also believe our answers are in the documentation, which the Atlantic reporter did not read."_ |
| Wired            | _"I arrived at my desk at 8:47am. I don't know what happened between the bedroom and the elevator."_                                                     |
| Consumer Reports | _"4.7 stars. We cannot fully explain this score."_                                                                                                       |
| The NYT          | _"None of them could explain why they signed up. All of them said they would do it again."_                                                              |
| Bloomberg        | _"98% compliance. This is higher than most medications."_                                                                                                |
| TechCrunch       | _"We asked for an interview with the Push. RISE said the Push does not give interviews. The Push arrived at our office at 8:52am. It stayed until 5pm."_ |
| The Guardian     | _"A bed that won't let you stay. In late capitalism, this passes for innovation. Four stars."_                                                           |

---

## The Help / FAQ Page — All 9 Answers

The FAQ page hero: _"If you are reading this, Push Mode is likely already running."_
Status badge: _"You were referred here from the RISE PM-1 remote."_

All 9 answers are worth preserving:

1. **Can Push Mode be turned off?** _"No...We recommend leaning into it."_
2. **Multiple button presses?** _"Each press confirms your original input...The bed has received your message. It will continue."_
3. **Wrong room?** _"Please check whether the room the bed delivered you to was, in fact, the right room. The bed's navigation has proven correct in 98% of cases where the user believed it to be incorrect."_
4. **Pillow not centered?** _"Please finish getting ready."_
5. **Bed followed me to work?** _"Yes. Most users report finding it reassuring within two to three weeks."_
6. **Stairs?** Full paragraph ending with _"There is no loyalty discount. We appreciate your patience and your purchase."_
7. **Nudge upgrade?** _"We respect the role it played in your mornings and do not offer trade-in credit."_
8. **How to stop Push Mode?** _"You would need to not press the button. We recognize this may be more difficult than it sounds."_
9. **The Push Pro?** _"We are not currently accepting questions about The Push Pro."_

Warranty: Push Mode: **lifetime**. Hardware: 5 years.

---

## Vision 2045 — The Escalation

5 vision versions (1.0–5.0, Q1 2021–Q1 2025). Notable: Vision 2.0 _"Children's product line added, then removed from same document."_

**5-Year (2030):** 2M units, 47 countries, _"Push Mode in Every Bedroom."_ Corporate wellness — _"HR departments are not the audience RISE imagined...They are highly motivated buyers."_ Municipal transit pilot: 34% on-time improvement.

**10-Year (2035):** _"RISE is not a bed company."_ Third-party integrations with coffee makers, smart homes. _"The bed knows your first meeting. It knows the traffic."_

**20-Year (2045):** Global morning infrastructure.

---

## Unbuilt / Planned Pages

These were discussed in conversation but never implemented:

| Page                    | Description                           | Status                               |
| ----------------------- | ------------------------------------- | ------------------------------------ |
| `/institute`            | RISE Sleep Science Institute          | Not built                            |
| `/trust`                | Trust/Security center (expanded)      | trust-center exists as "Coming Soon" |
| Changelog               | 18 entries + tombstone                | **Not found in current codebase**    |
| Status page             | Service status dashboard              | **Not found in current codebase**    |
| Careers                 | 6 job postings                        | **Not found in current codebase**    |
| Enterprise              | Enterprise sales page                 | **Not found in current codebase**    |
| `/index-score`          | RISE Index estimator                  | Not built                            |
| Compliance calculator   | Interactive calculator                | Not built                            |
| Referral dead-end       | Referral flow that leads nowhere      | Not built                            |
| Community/Forum         | Community page                        | Not built                            |
| Accessibility statement | —                                     | Not built                            |
| Reviews (Supabase)      | User reviews with Drizzle ORM         | Specced, not built                   |
| OG images               | Social media preview images           | Not built                            |
| Spotify playlists       | MCP-generated playlists               | Script exists, not executed          |
| Light mode CSS          | Full light mode polish                | Not done                             |
| Blog rebranding         | Replace Radiant placeholder in Sanity | Not done                             |

**Note:** The conversation summary referenced changelog, status, careers, and enterprise pages as "completed" with specific content, but these do not exist in the current codebase. Either they were discussed/designed but not committed, or they exist in a branch that wasn't merged. The current `ai/chore/remove-trademark-symbols` branch and `main` should be checked.

---

## The Master Timeline — Canonical Chronology

| Date             | Event                                                                                                                                                      | Source                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 2009             | RISE founded by Dr. Eleanor Voss                                                                                                                           | About page                     |
| 2011             | RISE Ambient + RISE Tone (first products, both fail)                                                                                                       | About page, Product Graveyard  |
| 2012             | Thermal, Gradient, Alarm (all fail — users adapt)                                                                                                          | About page                     |
| 2013             | NudgeSense, NudgeLight (app 4.8★, product 2.1★)                                                                                                            | About page                     |
| 2014             | NudgeWarm, NudgeTone (+23 min sleep — made it worse)                                                                                                       | About page                     |
| 2015             | NudgeEdge (lateral tilt — 100% rolled back)                                                                                                                | About page                     |
| 2016             | NudgeBar (74% compliance — cult following)                                                                                                                 | About page                     |
| Nov 14, 2018     | Nudge discontinuation memo (DOC-002) — written at 6:47am                                                                                                   | Internal docs                  |
| 2019             | RISE Nudge (RN-01) consolidated line, later discontinued                                                                                                   | Product page                   |
| FY2020           | Revenue: $2.1M, 940 units, 12% margin                                                                                                                      | Financials                     |
| Q1 2021          | Vision 1.0 written                                                                                                                                         | Vision page                    |
| Jan 3, 2021      | Dr. Voss's Push configured — Unit RSB-0000000000000001                                                                                                     | DOC-003                        |
| Jan 4, 2021      | Voss's first on-time meeting (7:47am) — "She was there before the meeting existed"                                                                         | DOC-003                        |
| 2021             | The Push launches. Revenue: $8.4M (+300%), 3,800 units                                                                                                     | Financials, Shareholder Letter |
| Mar 14, 2022     | SC-0047 — The Coffee Shop (Valencia St, SF)                                                                                                                | DOC-007                        |
| Apr 1, 2022      | DOC-008 — RISE Index Methodology published (April Fools' Day)                                                                                              | Internal docs                  |
| FY2022           | Revenue: $23.7M (+182%), 10,600 units                                                                                                                      | Financials                     |
| Mar 15, 2023     | DOC-006 — HR Workplace Waiver created (still "Awaiting Legal Review")                                                                                      | Internal docs                  |
| Sep–Nov 2023     | Marketing consultant produces DOC-010 through DOC-019                                                                                                      | Internal docs                  |
| Sep 3, 2023      | SC-0089 — The Street Fair (Hayes Valley, SF)                                                                                                               | DOC-007                        |
| FY2023           | Revenue: $38.2M (+61%), 17,100 units                                                                                                                       | Financials                     |
| Jan 9, 2024      | DOC-019 — Retroactive proof of concept for a product on market since 2021                                                                                  | Internal docs                  |
| Feb 8, 2024      | SC-0112 — The Dog (Noe Valley, SF)                                                                                                                         | DOC-007                        |
| Aug 12, 2024     | **Arvin Reyes's last day.** Last deploy. Last login (9:43am). Last key rotation. Last SOC 1 update. Last Trust Center update. Session token: still active. | Everything                     |
| Aug 14, 2024     | Press release: 98% compliance rate (2 days after Arvin left)                                                                                               | Press page                     |
| Oct 22, 2024     | SC-0134 — The Parking Ticket (SOMA, SF) — "unattended motorized mattress of unknown origin"                                                                | DOC-007                        |
| Nov 8, 2024      | Series C: $120M                                                                                                                                            | Press page, Financials         |
| Jan 15, 2025     | DOC-001 — Q4 2024 Incident Log compiled                                                                                                                    | Internal docs                  |
| Feb 1, 2025      | DOC-009 — Audio Data Access Log Q1 2025                                                                                                                    | Internal docs                  |
| Feb 3, 2025      | RISE Move press release — "We are aware of the stairs"                                                                                                     | Press page                     |
| Feb 12, 2025     | IT notified about sitemap containing internal routes                                                                                                       | Sitemap footer                 |
| Mar 1, 2025      | Sitemap generated (internal routes still listed)                                                                                                           | Sitemap                        |
| Mar 1, 2025      | Dr. Voss's shareholder letter — written at 6:47am                                                                                                          | Shareholder Letter             |
| Mar 1, 2025      | DOC-005 — Move Engineering Status (stair navigation RED)                                                                                                   | Internal docs                  |
| Mar 14, 2025     | AGM: 10:04am–2:31pm. Override proposal defeated (3%). "Yes. Next question."                                                                                | Meeting Minutes                |
| Apr 2025         | S-1 filed                                                                                                                                                  | Financials                     |
| FY2024           | Revenue: $89.4M (+134%), 47,000 units, 68% margin, 340K waitlist                                                                                           | Financials                     |
| Q3 2026 (target) | IPO                                                                                                                                                        | Financials                     |

---

## The Unspoken Rules — What Makes It Work

These are the meta-principles that govern the fiction. They are never stated in the website but must be followed by anyone contributing:

1. **Nobody at RISE thinks anything is wrong.** Every document, every FAQ answer, every legal clause is written by someone who believes they are doing excellent, responsible work. The comedy is structural, never vocal.

2. **The bed always works.** There are no malfunctions. Every "incident" is the system operating correctly in an unexpected context. INC-2415: the bed was right, the user's calendar was wrong.

3. **Arvin is sympathetic.** He's not incompetent — he's a junior dev who ran out of time and whose manager didn't ask the right questions. His farewell note is genuine. He liked the job. The Push helped him get up. His auth middleware was "mostly there."

4. **Dr. Voss is not a villain.** She is an extremely competent founder who has never been late since 2021 and who genuinely believes the product improves lives. Her Resistance Index is 0.2 out of 10. She doesn't need the bed — she agrees with it.

5. **James Park is doing his job.** Every legal document is thorough, accurate, and defensive. He's a good lawyer. The fact that the product he's defending is absurd is not his problem. He confirmed Appendix C exists. Next question.

6. **Every number is consistent.** 98% compliance, 340K waitlist, $89.4M revenue, 47,000 units, 2,048 sensors, 64×32 grid, 8-meter audio pickup, 4-second buffer — these numbers appear in multiple places and must never contradict.

7. **Time moves.** The `daysSinceArvin()` counter, the dynamic login times, the "always recent" external IP timestamps — these make the system feel alive. The fiction is happening right now.

8. **Absence is content.** The redacted RISE Index methodology, the unbuilt auth middleware, the empty media library, the reverting settings — what doesn't work tells the story as much as what does.

9. **The exclamation point matters.** "Have a productive day!" is the only one. It appears on the remote's fine print. Its warmth, in context, is the most unsettling thing on the entire site.

10. **The bed has more agency than the user.** It navigates, it commutes, it waits, it returns. It makes itself. It follows you to work. It was correct 98% of the time when the user believed it was incorrect. The bed is the real protagonist — of the product, the film, and the website.

---

---

# PART TWO: BREAKING THE FOURTH WALL

_Everything below this line documents what is actually happening behind the scenes — the hidden systems, the narrative threads, the things nobody says out loud, and the factual timeline that holds the fiction together. This exists so that any future collaborator, AI session, or the creators themselves can verify whether a detail is consistent, intentional, or a gap._

---

## The Actual Route Map (Verified April 2026)

The conversation history referenced "43 routes." The actual count of distinct page components:

### Consumer Routes (9)

| Route             | Component                        | Description                                                           |
| ----------------- | -------------------------------- | --------------------------------------------------------------------- |
| `/`               | `(site)/page.tsx`                | Homepage — hero video placeholder, testimonials, stats bar            |
| `/about`          | `(site)/about/page.tsx`          | Full product timeline 2009–present, 4 principles, by-the-numbers grid |
| `/products/push`  | `(site)/products/push/page.tsx`  | The Push product page — SOLD OUT                                      |
| `/products/nudge` | `(site)/products/nudge/page.tsx` | The Nudge — PERMANENTLY DISCONTINUED                                  |
| `/move`           | `(site)/move/page.tsx`           | RISE Move teaser — VNS subscription, stair navigation                 |
| `/activate`       | `(site)/activate/page.tsx`       | 12-stage interactive configurator with canvas                         |
| `/help`           | `(site)/help/page.tsx`           | FAQ — 9 questions, all devastating                                    |
| `/blog`           | `(site)/blog/page.tsx`           | Sanity CMS-powered blog (placeholder content)                         |
| `/blog/[slug]`    | `(site)/blog/[slug]/page.tsx`    | Individual blog post                                                  |

### Platform Routes (3)

| Route                | Component                           | Description                                      |
| -------------------- | ----------------------------------- | ------------------------------------------------ |
| `/data-request`      | `(site)/data-request/page.tsx`      | 10-step Kafkaesque DSAR gauntlet                 |
| `/sdk`               | `(site)/sdk/page.tsx`               | DataKit SDK — 3 pricing tiers, waitlist Catch-22 |
| `/sdk/documentation` | `(site)/sdk/documentation/page.tsx` | 8 known issues, API reference "coming soon"      |

### Investor Routes (7)

| Route                           | Component                                      | Description                                   |
| ------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| `/investors`                    | `(site)/investors/page.tsx`                    | Investor relations hub                        |
| `/investors/vision`             | `(site)/investors/vision/page.tsx`             | Vision 2045 — 5/10/20-year escalation         |
| `/investors/shareholder-letter` | `(site)/investors/shareholder-letter/page.tsx` | Dr. Voss's FY2024 letter                      |
| `/investors/annual-report`      | `(site)/investors/annual-report/page.tsx`      | Annual report with 8 risk factors             |
| `/investors/meeting-minutes`    | `(site)/investors/meeting-minutes/page.tsx`    | March 2025 AGM — 9 Q&As, 5 resolutions        |
| `/investors/financials`         | `(site)/investors/financials/page.tsx`         | Interactive Recharts — revenue, NPS, waitlist |
| `/investors/press`              | `(site)/investors/press/page.tsx`              | 10 press quotes, all beautifully wrong        |

### Legal Routes (7)

| Route                          | Component                                     | Description                              |
| ------------------------------ | --------------------------------------------- | ---------------------------------------- |
| `/legal`                       | `(site)/legal/page.tsx`                       | Legal document hub                       |
| `/legal/terms`                 | `(site)/legal/terms/page.tsx`                 | Terms of Service — 25 sections           |
| `/legal/privacy`               | `(site)/legal/privacy/page.tsx`               | Privacy Policy — 31 sections             |
| `/legal/push-mode-eula`        | `(site)/legal/push-mode-eula/page.tsx`        | Push Mode EULA — 19 sections             |
| `/legal/sleep-data-policy`     | `(site)/legal/sleep-data-policy/page.tsx`     | Sleep & Environmental Data — 14 sections |
| `/legal/autonomous-navigation` | `(site)/legal/autonomous-navigation/page.tsx` | Autonomous Navigation — 11 sections      |
| `/legal/disclaimer`            | `(site)/legal/disclaimer/page.tsx`            | General Disclaimer — 8 sections          |

### Security Routes (2)

| Route                    | Component                               | Description                                             |
| ------------------------ | --------------------------------------- | ------------------------------------------------------- |
| `/security`              | `(site)/security/page.tsx`              | 6 certs (all pending), 8 features, 5 progress bars      |
| `/security/trust-center` | `(site)/security/trust-center/page.tsx` | "Coming Soon" — ETA Q4 2024. Last updated Aug 12, 2024. |

### Press Routes (2)

| Route                           | Component                                      | Description                     |
| ------------------------------- | ---------------------------------------------- | ------------------------------- |
| `/press`                        | `(site)/press/page.tsx`                        | 4 press releases                |
| `/press/rise-move-announcement` | `(site)/press/rise-move-announcement/page.tsx` | Move announcement — Feb 3, 2025 |

### Internal System Routes (5)

| Route                   | Component                       | Description                                                |
| ----------------------- | ------------------------------- | ---------------------------------------------------------- |
| `/internal`             | `internal/page.tsx`             | Document management index — Payload CMS clone              |
| `/internal/docs/[slug]` | `internal/docs/[slug]/page.tsx` | Individual document viewer — 10 full + 10 stubs + 1 secret |
| `/internal/users`       | `internal/users/page.tsx`       | 3 user accounts (1 should be deactivated)                  |
| `/internal/media`       | `internal/media/page.tsx`       | Empty — uploads fail ("S3 not connected")                  |
| `/internal/settings`    | `internal/settings/page.tsx`    | All toggles revert. Nothing persists.                      |

### Hidden Routes (2)

| Route                               | Component         | Description                                |
| ----------------------------------- | ----------------- | ------------------------------------------ |
| `/remote`                           | `remote/page.tsx` | PM-1 Remote interactive simulation         |
| `/internal/docs/arvin-final-commit` | (via slug route)  | Arvin's goodbye — not in index, not in CMS |

### Utility Routes (3)

| Route          | Component              | Description                                             |
| -------------- | ---------------------- | ------------------------------------------------------- |
| `/sitemap`     | `sitemap/page.tsx`     | HTML sitemap (includes internal routes "in error")      |
| `/sitemap.xml` | `sitemap.xml/route.ts` | XML sitemap                                             |
| `/robots.ts`   | `robots.ts`            | Disallows `/internal/`, `/remote/`, `/studio/`, `/api/` |

### Studio Route (1)

| Route     | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| `/studio` | Sanity Studio — blog CMS (still has placeholder Radiant template data) |

**Total distinct page components: ~41** (excluding layouts, not-founds, and error boundaries). The internal `[slug]` route alone serves 21 different documents, so the "page count" is higher than the component count.

---

## The Arvin Reyes Thread — Complete Lore

Arvin Reyes is the connective tissue of the internal system. He is a fictional junior developer who worked at RISE, built the internal document management system, and left on **August 12, 2024** without finishing critical infrastructure. His presence is felt across the entire codebase through TODO comments, timestamp references, and system failures.

### What Arvin Built

- The internal document management system (modeled after Payload CMS)
- The document schema with an `isPublic` field that **defaults to true**
- The user table (3 accounts: Dr. Voss, James Park, himself)
- The media library (upload UI exists but "S3 not connected")
- The settings page (permissions matrix, access control — none persisted)

### What Arvin Did NOT Build

- **Authentication middleware** — the file `auth-middleware-draft.ts` is referenced in his farewell note but never existed in the codebase. He got 80% through, then Payload's docs changed and he lost a week.
- **The `isPublic` toggle** — the schema field exists and defaults to true. The UI toggle to change it was never built. Everything is public.
- **Session token expiry** — his account `areyes@riseawake.com` still shows as active with a session token that has no expiry function.
- **S3 connection** — the media upload zone exists but drops to an error toast: "Storage connection not configured."
- **Settings persistence** — the permissions matrix and access level selector both revert to defaults (all enabled, public) after 1 second or on page reload. The `POST /api/settings` endpoint was never created.
- **The audit log** — referenced in the permissions matrix but never implemented.
- **Bulk actions** — the document index has Archive and Delete bulk actions. The code comment reads: `"bulk actions do nothing. arvin."`

### Arvin's TODO Comments (Scattered Through Codebase)

| Location                             | Comment                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| `internal-docs.ts` (top)             | `"TODO: connect to actual DB (currently using hardcoded data)" — areyes, Aug 12 2024` |
| `media/page.tsx`                     | `{/* TODO: connect to S3 bucket — areyes */}`                                         |
| `settings/page.tsx` (access control) | `{/* TODO: wire this to middleware — areyes */}`                                      |
| `settings/page.tsx` (save)           | `{/* settings are not saved — arvin */}`                                              |
| `settings/page.tsx` (API)            | `{/* TODO: POST /api/settings — areyes */}`                                           |

### The Arvin Timeline

| Date                 | Event                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Unknown              | Hired as Developer at RISE                                                                                                                     |
| Unknown–Aug 2024     | Built the internal CMS. Copied Payload CSS tokens from source ("They are correct.")                                                            |
| Aug 12, 2024, 9:43am | Last login to the internal system                                                                                                              |
| Aug 12, 2024         | Last deployment. Last key rotation. Last SOC 1 documentation update. Last Trust Center update.                                                 |
| Aug 12, 2024         | Left RISE. Account not deactivated. Session token active. No expiry. The function that would check it was never written.                       |
| Post-departure       | Nobody has deployed since. The Settings page shows `daysSinceArvin()` days since last deploy and `sprintsSinceArvin()` 2-week sprints overdue. |

### The Secret Arvin Page

`/internal/docs/arvin-final-commit` is a secret route. It is:

- **NOT** in the `DOC_SEEDS` array (doesn't appear in the document index table)
- **NOT** discoverable through the internal system's navigation
- Accessible only by direct URL
- Referenced in the `/internal/not-found.tsx` page as a nearly invisible 1px link at 4% opacity (`aria-hidden`, `tabIndex={-1}`, `userSelect: none`)
- Listed in the HTML sitemap under "Hidden" (with no description)

**The farewell note content** is a monospace plain text file (`arvin-final-commit.txt`). Key revelations:

- The auth middleware is in `auth-middleware-draft.ts` — "i never finished it"
- The `isPublic` field defaults to true — "the toggle is not built. everything is public."
- James Park never asked about access control directly — he asked if "the CMS was working," Arvin showed him the document list, it looked correct, Park said "good job"
- Dr. Voss's personal configuration (DOC-003) is public — "i know"
- Push Mode compliance data (DOC-001) is public — "i know"
- His session token in the users table is still active — "nobody deactivated it. i don't know why i'm telling you this."
- "the bed does follow you to work. i thought it was a bug. it's in the specs. i read them after."
- "if dr voss reads this: i did get up on time every morning while i worked here. the push mode helped. i mean that sincerely."

The bottom of the page reads: _"This file is not accessible from the document index. It is accessible from this URL. RISE IT has not been notified. RISE IT is not aware. RISE IT response time: variable."_

---

## The Breach Tracking System — How It Actually Works

The internal system has a layered tracking mechanism that tells a story through escalating resignation. The code lives in `internal-tracker.ts` and `internal-time.ts`.

### The Asymmetry (The Joke)

A code comment at the top of the tracker file states: _"The login is sessionStorage (ephemeral). The tracking is localStorage (permanent). The asymmetry IS the joke."_

There is no login. There is tracking.

### What Gets Tracked

- Visitor IP (fetched from ipify API on first visit to `/internal`)
- Each document viewed: document ID, first-seen timestamp, last-seen timestamp
- A counter called `itNotifications` that increments with every new document visited

### The Escalating IT Security Narrative

The PayloadShell component displays a "security alert" toast on first visit showing the visitor's IP. As the visitor views more documents, the tone of the breach notification changes:

| Docs Viewed | Tone                      | Example Language                                                                                                                                                                                                              |
| ----------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–2         | Factual                   | Standard access logging                                                                                                                                                                                                       |
| 3–5         | Resigned                  | _"IT security has been aware for some time"_                                                                                                                                                                                  |
| 6–9         | Deeply resigned           | —                                                                                                                                                                                                                             |
| 10+         | Institutionally exhausted | _"IT security has been notified [N] times today. IT security is, in a meaningful sense, aware of what is happening. No access restriction has been applied...it was in Arvin's final sprint. Arvin left on August 12, 2024."_ |
| 15+         | Respectful                | _"probably knows more about this system than most people who work here"_                                                                                                                                                      |

### Dynamic Time Functions

`internal-time.ts` provides:

- `daysSinceArvin()` — days since August 12, 2024
- `sprintsSinceArvin()` — 2-week sprints since August 12, 2024
- `vossLoginTime()` — always "Today, [time]" (1–4 hours ago, seeded PRNG)
- `parkLoginTime()` — similar dynamic login time for James Park
- Staff access times use seeded PRNG that changes hourly — feels alive but stays stable within the same hour
- External IP access times show 1–180 minutes ago — _"always recent, always unsettling"_

---

## The Internal Document System — Complete Content Guide

### Documents with Full Rendered Content (10 + 1 Secret)

**DOC-001: Push Mode Incident Log — Q4 2024** (CONFIDENTIAL, Jan 15 2025)
23 incidents, 91% resolution rate. 12 detailed. Highlights:

- INC-2403: Unregistered occupant detected. _"Second occupant now logged as 'Visitor (recurring)'"_ — the bed doesn't care about your personal life, it just logs it.
- INC-2415: Bed anticipated departure incorrectly. _"Telemetry confirmed bed was correct. User's calendar had been updated."_ — the bed was right. The user's calendar was wrong.
- INC-2428: User placed object in path. _"Bed navigated around object on attempt 1. Through object on attempt 2. Object replaced."_ — the bed destroyed the obstacle, then replaced it.
- INC-2431: Push Mode activated outside registered address. _"Button was pressed by a house guest."_ — the guest was routed. The guest has not been contacted.
- INC-2440: Push Mode activated at 5:47am on December 25. _"Push Mode operated as designed."_ — Christmas is not an exception.
- QA sub-log access portal has returned 404 since October. IT is aware.

**DOC-002: Nudge Discontinuation Memo** (INTERNAL, Nov 14 2018)
Dr. Voss's memo killing the Nudge line. 7 product variants and their compliance rates (62–74%). The pivotal declaration: _"There is a ceiling on what suggestion can achieve. We have found the ceiling. We are going to go through it."_ And: _"It will not ask. It will not suggest. It will not wait. There will not be an off switch."_

Written at 6:47am. The note at the bottom: _"Push Mode was not available in 2018. Dr. Voss got up on her own. She has not been asked to explain how."_

**DOC-003: Dr. Voss — Personal Push Configuration** (DR. VOSS EYES ONLY, Jan 3 2021)

- Serial: **RSB-0000000000000001** — Unit 1. The first Push ever made.
- Target wake: 6:00:00am — _"Precise to the second. She set it herself."_
- Resistance Index: **0.2 / 10.0** — lowest in the RISE user base. She doesn't resist.
- RISE Index Score: **[REDACTED]** — _"Dr. Voss redacted this field personally."_
- Morning sequence: 26 min configured, **19 min 24 sec** actual. She's faster than her own configuration.
- She removed the rug after Day 3. _"It was slowing things down."_
- Fastest activation on record: 22 minutes (34 min faster than second place).
- DR. VOSS EYES ONLY warning: _"access control for this classification tier was not implemented. It is in Arvin's TODO list. Arvin is no longer at RISE."_

**DOC-004: Push Pro Development Notes** (RESTRICTED, Various)
Almost entirely REDACTED. Unredacted table of contents reveals:

- "4.1 The Feature We Are Not Naming Yet"
- "4.2 Off Switch (Section Archived — See Note)" — flagged yellow
- Dr. Mara Chen's note on the off switch: _"There will not be an off switch in the Push Pro."_
- _"Appendix B — The Compliance Data (Dr. Voss Note: Don't Put This In The Document)"_
- _"availability does not constitute disclosure"_ — the document being readable doesn't mean RISE has disclosed anything.

**DOC-005: RISE Move Engineering Status Report** (CONFIDENTIAL, Mar 1 2025)
11 workstreams with traffic-light status. Solo commute stair navigation: **RED**. Overall timeline: **RED**.

Section 4.1 — Controlled Descent Failure Analysis — is the most technically detailed thing on the site:

- 4 solo commute descent tests. 3 successful. **Test 4 was not** (forward topple).
- _"An uncontrolled 80-120 lb object falling down a staircase is not a product. It is a liability."_
- Sensor-to-brake latency: 340ms current, sub-200ms target. Only 60ms margin of error.
- Required: 100 consecutive successful unattended 12-step descents. Current: 3.
- Dr. Voss's note: _"Test 4 is why there is no timeline. Work on Test 5."_

**DOC-006: HR Push Mode Workplace Waiver** (INTERNAL, Mar 15 2023)
Template waiver for corporate wellness programs. Status: **Awaiting Legal Review since March 2023** — over 3 years and counting.

- Section 7: _"my employer requested this capability...I acknowledge that I was not present for this discussion."_
- Section 14: _"I acknowledge that neither I nor my employer has read the Privacy Policy in full. I acknowledge that this acknowledgment constitutes acceptance regardless."_
- HR/Legal impasse: _"HR considers this to be Legal's responsibility. Legal considers this to be HR's responsibility. The document remains in use."_

**DOC-007: Solo Commute Incident Archive** (CONFIDENTIAL, Ongoing)
4 selected incidents from SC-0001 through SC-0147 (implying 147+ solo commute incidents on file):

- **SC-0047 — The Coffee Shop** (Mar 14 2022, Valencia St SF): Bed entered through propped-open door, went 8 feet in, reversed. Displaced one ceramic mug. _"The shop posted about it on Instagram. 17,000 likes."_ The shop is now a landmark.
- **SC-0089 — The Street Fair** (Sep 3 2023, Hayes Valley SF): Bed waited 4 hours in obstacle hold protocol during a street fair. Arrived home at 1:14pm (standard: 11 min). The user arrived home first. Found the bed at the door. _"The bed was making itself."_
- **SC-0112 — The Dog** (Feb 8 2024, Noe Valley SF): Neighbor's dog followed bed for 6 blocks, making matching lateral adjustments. _"The dog has been observed to wait at the corner where it previously encountered the bed on subsequent mornings."_ Incident redacted per _"RISE animal privacy policy, Section 4, which does not exist but which was referenced in the incident notes and has now been formally established by legal as a retroactive policy."_ — a policy created retroactively to cover a citation to a policy that didn't exist.
- **SC-0134 — The Parking Ticket** (Oct 22 2024, SOMA SF): Officer issued citation to bed, which has no license plate. _"The citation was issued to a fire hydrant."_ Supplemental police report describes the device as _"an unattended motorized mattress of unknown origin."_

**DOC-008: RISE Index Methodology** (RESTRICTED, Apr 1 2022)
Table of contents with 5 sections and 2 appendices. **All 5 methodology sections are entirely REDACTED.** Appendix A: _"The Index Is Working As Intended."_ Appendix B: _"See Appendix A."_

- Published on April 1, 2022 (April Fools' Day — date is deliberate).
- _"The full methodology is available to: Dr. Voss. Mara Chen. Thomas Ellery. The document server. Apparently also whoever is reading this."_

**DOC-009: Audio Data Access Log — Q1 2025 Summary** (CONFIDENTIAL, Feb 1 2025)
Audio data collection audit. The _"Other"_ category is under review. The distribution list was last audited in 2019.

**SECRET: arvin-final-commit.txt** (INTERNAL, Aug 12 2024)
[See "The Arvin Reyes Thread" section above for full content.]

### Documents That Are Metadata-Only Stubs (10)

DOC-010 through DOC-019 exist in the index table with titles, word counts, classification levels, and dates — but render "Document content not available" when opened. They are the **marketing consulting archive** — a series of documents produced by an unnamed external growth marketing consultant:

| ID      | Title                                         | Key Satirical Detail in Summary                                                                                             |
| ------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| DOC-010 | Headline Swipe File & Performance Analysis    | _"The consultant's invoice has not been paid."_                                                                             |
| DOC-011 | Buyer Agenda Matrix & Conflict Resolution     | _"The Mourner agenda scored higher than expected."_                                                                         |
| DOC-012 | Attention Cluster & Reptilian Trigger Mapping | _"Reptilian brain trigger mapping. The consultant described the product as 'a marketer's dream.'"_ — Awaiting Legal Review  |
| DOC-013 | StoryBrand SB7 Playbook                       | _"The villain is Monday morning. The guide is RISE. The call to action is one button."_                                     |
| DOC-014 | Brand Identity Suite (Mission/Vision/WHY)     | _"Dr. Voss described the WHY statement as 'close but not right yet.'"_                                                      |
| DOC-015 | Content Marketing Blog Playbook               | Active                                                                                                                      |
| DOC-016 | Customer Avatar Canvas Worksheet              | _"Avatar name: David K. Section 9 was crossed out and rewritten by Dr. Voss."_ — Dave from the film                         |
| DOC-017 | Value Journey Worksheet & Action Plan         | _"The Excite stage has the longest entry. The Convert stage notes the product is sold out."_                                |
| DOC-018 | Sub-Testimonial & Social Proof Strategy       | Awaiting Legal Review                                                                                                       |
| DOC-019 | Proof of Product Concept Validation Report    | _"Retroactive proof of concept validation. The product has been on the market since 2021. The waitlist is 340,000 people."_ |

The marketing docs are all from Sep–Jan 2023/2024, the consultant is never named, the invoice was never paid, and the "Reptilian Trigger Mapping" document is awaiting legal review.

---

## The Payload CMS Simulation — Construction Details

The `/internal` system is designed to look like a real Payload CMS admin panel that a junior developer deployed without authentication. Here's what's actually happening:

### PayloadShell Component

`PayloadShell.tsx` renders the entire admin chrome — sidebar nav, breadcrumbs, top bar, toast system. It uses pixel-accurate Payload CSS tokens (code comment: _"Arvin copied these from the Payload source. They are correct."_).

### The Sidebar Navigation

Left nav shows: Documents (the only real section), Media (empty), Users (3 accounts), Settings (doesn't persist). The sidebar also shows a "RISE Internal" logo at top and dynamic counts.

### The Toast System

`fireToast()` is a global function that mimics Payload's notification system. It fires for:

- Security alerts (IP on first visit)
- Upload failures on Media page ("Storage connection not configured")
- Settings "saves" that don't persist
- Bulk action attempts that do nothing

### The Settings Page — Everything Reverts

The Settings page is the most conceptually pure joke in the internal system:

- **Access Control**: Three options — Public, Authenticated, Private. You can click any of them. The selection reverts to "Public" after 1 second. Warning text appears: _"Access level change will not take effect until the auth middleware is implemented."_ Below: _"Current effective access level: Public (default — not overridable until middleware is complete)"_
- **Permissions Matrix**: 7 collections × 4 permission types (Read/Create/Update/Delete). All toggles are on. You can toggle any off. It reverts after 1 second. _"Changes to this matrix are not persisted between sessions. All permissions reset to default (all enabled) on page reload. This is because the settings API endpoint was not implemented."_
- **System Info** shows: CMS Version: Payload v3.0.0-beta.67, Database: Not connected (hardcoded data), Auth Middleware: Not implemented, Last Deployed: August 12, 2024 (`daysSinceArvin()` days ago), Deployed By: areyes@riseawake.com, Next Planned Deployment: Next sprint (date TBD) — `sprintsSinceArvin()` sprints overdue, Known Issues: "See Arvin's TODO comments throughout codebase"
- **Save Button**: Shows "Saving..." for 700ms, shows a success toast, saves nothing. Code comment: `// nothing saved. arvin.`

### The Users Page

Three accounts:

1. **Dr. Eleanor Voss** — Super Admin — `evoss@riseawake.com` — Last Login: dynamically shows "Today, [1–4 hrs ago]" — she's always logged in recently
2. **James Park** — Admin — `jpark@riseawake.com` — Also shows recent dynamic login
3. **Arvin Reyes** — Developer — `areyes@riseawake.com` — Last Login: **Aug 12, 2024, 9:43am** (static, never changes) — Status: **Active** — Yellow warning: _"Account not deactivated. Session token active. No expiry. The function that would check it was never written."_

### The Media Page

Empty library. A drag-and-drop upload zone exists. Any attempt to upload fires: _"Upload failed. Storage connection not configured."_ Bottom text: _"0 files · Storage: not configured · S3 bucket: not connected"_. An invisible `TODO: connect to S3 bucket — areyes` sits in the markup.

---

## The PM-1 Remote Page — Interaction Design

`/remote` is a black page with film grain overlay. The PM-1 remote is rendered as a pill-shaped body (88px wide) with a single glowing circular button (52px) and the RISE logo etched at the top.

### State Machine

| State          | Visual                     | Text                                |
| -------------- | -------------------------- | ----------------------------------- |
| **Idle**       | Warm white pulse on button | "PM-1 · Ready" (pulsing)            |
| **Activating** | Glow intensifies to 100%   | "Activating..."                     |
| **Routing**    | Steady glow                | 11-step sequence, ~10 seconds total |
| **Complete**   | Glow fades                 | "Have a productive day."            |

### The 11-Step Routing Sequence

1. "Push Mode initializing..."
2. "Mapping morning sequence..."
3. "Calibrating nudge force..."
4. "STATE THREE: engaging..."
5. "Routing to bathroom..."
6. "Routing to closet..."
7. "Self-making sequence: initiated..."
8. "Routing to kitchen..."
9. "Coffee detected. Vessel: unknown."
10. "Routing to departure point..."
11. "Push Mode complete. Have a productive day."

### Behavioral Details

- **During routing**: A `beforeunload` handler warns _"Push Mode cannot be interrupted once initiated. This is a feature, not a limitation."_ — the browser literally won't let you leave clean.
- **Multiple presses** (>2 during routing): A message appears in 9px italic at 10% opacity — _"Push Mode noted your input (Nx). Push Mode is continuing."_ — barely visible, perfectly patronizing.
- **After completion**: _"The bed is returning home. It will be there when you get back."_ + Return Home link.

### Fine Print

At the bottom of the idle remote: _"Push Mode cannot be manually interrupted once initiated. This is a feature, not a limitation. Have a productive day!"_ — the only exclamation point in the entire brand.

---

## The Activate Page — 12-Stage Configurator

The activation flow is a multi-step wizard with interactive elements. Each stage has a title, estimated duration, and content that escalates the commitment.

### Key Interactive Elements

- **Intensity Dial** (Stage 1): 4 levels — Gentle, Standard, Committed, **Non-Negotiable** (_"Full Push Mode. No transition period. Immediate vertical delivery."_). A bed silhouette SVG tilts based on the selected intensity.
- **Morning Sequence Builder** (Stage 4): Drag-and-drop reorderable items. _"Duration estimates are monitored. Persistent underestimation results in automatic adjustment."_
- **Environment Canvas** (Stage 5): Flagged as ⚠. _"Staircase navigation is not supported. See RISE Move."_
- **Serial Number Entry** (Stage 12): Triggers a refund warning — _"refund window has closed"_ upon entry. No undo.

### The 8 Final Acknowledgments

All must be accepted at Stage 12 — "Review & Activate":

1. Push Mode cannot be interrupted.
2. Refund window closed upon serial number entry.
3. Environmental incompatibilities not grounds for refund.
4. Staircase not supported.
5. Duration estimates monitored.
6. GPS shared with autonomous navigation.
7. _"The bed infers outfit correctness from time and behavior. It cannot see."_
8. Intensity calibrated automatically, manual adjustment not available.

### Sleep Position Options

Includes: _"I don't know — The bed will determine this."_

---

## The Data Request Page — The Complete Gauntlet

The 10-step DSAR process is designed to be technically compliant while being practically impossible. Every step is real enough that a privacy regulator might nod, while a human being would weep.

### Step-by-Step Brutality

1. **Determine Request Type** — 5 types (A–E). Type E creates a catch-22: _"RISE cannot confirm whether you appear in occupancy data without first processing a request."_
2. **Obtain Form DSR-01** — Not downloadable. Options: postal mail (15–20 days), hotline (**Mon–Fri, 11:00–11:30am PT, 40–70 min hold, no callback**), or in-person (**third Tuesday of each quarter, 2:00–2:45pm, by appointment**). Must use **black or dark blue ballpoint pen**. Correction fluid invalidates.
3. **Complete DSR-01** — 34 pages. Device serial found _"by lying on the floor beneath the bed with a light source and reading upward."_ Handwritten 100–200 word statement citing one of **47 approved reasons in Schedule 3**. Reason 23: "Personal Curiosity" — accepted, +45 days processing, +$25 surcharge.
4. **Pay Processing Fee** — $35–$150 by type. Audio: +$200. **Certified check or money order only.** RISE acknowledges the irony of requiring credit card details for ID verification while not accepting cards.
5. **Assemble & Submit** — Certified mail, numbered dividers, self-addressed stamped envelope. _"If the package is lost in transit, the process restarts from Step 1."_
6. **Receive Acknowledgment** — 20–30 business days by standard post.
7. **Identity Verification Call** — Scheduled by letter. 3 time slots. **From an unregistered number.** Must confirm exact date of first Push Mode activation. Two failed attempts voids the request.
8. **Wait** — **90 business days.** Paused for company holidays (_"Appendix G — forthcoming"_). Data in .rsm format (proprietary).
9. **Receive Data** — USB-A flash drive by standard post. Requires **DataKit SDK ($299–$2,400)** to open. Waitlist: 4,891 developers.
10. **Return Delivery Confirmation Card** — Within 21 days or **data is remotely wiped.** _"RISE respectfully notes that if you have reached Step 10 and are considering not returning the Confirmation Card, this would be an unusual conclusion to a 6–18 month process."_

### Cross-References

The data request process connects to the SDK page (you need DataKit to open your own data), the SDK waitlist (4,891 deep), the .rsm proprietary format, and Appendix G (the company holiday schedule, also referenced in meeting minutes action items — "forthcoming" everywhere, published nowhere).

---

## The Meeting Minutes — Every Q&A Exchange

The March 14, 2025 AGM minutes contain 9 Q&A exchanges. These are the primary vehicle for shareholder confusion meeting corporate certainty.

| #   | Question                                              | Who Answers | Key Line                                                                                                                                                          |
| --- | ----------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Manual override?                                      | Dr. Voss    | _"Users who retain an override use it...We will not be adding one."_                                                                                              |
| 2   | 340K waitlist — supply or strategy?                   | Dr. Voss    | _"Both...The waitlist is, in some ways, part of the product."_                                                                                                    |
| 3   | What's in Appendix C?                                 | James Park  | _"I can confirm it exists. Next question."_                                                                                                                       |
| 4   | Push Pro timeline?                                    | Dr. Voss    | _"It exists. It is in development. That is what we are saying today."_                                                                                            |
| 5   | Autonomous navigation legal status?                   | James Park  | _"The user authorized the commute by pressing the button."_                                                                                                       |
| 6   | Stairs                                                | Shareholder | _"My apartment has stairs. The bed stops at the bottom every morning."_ → Dr. Voss: _"It is being worked on. It will not be free. There is no loyalty discount."_ |
| 7   | **"My wife says our Push is following her to work."** | Dr. Voss    | **"Yes. Next question."**                                                                                                                                         |
| 8   | Audio data extent?                                    | James Park  | Standard privacy policy reference, Section 19.                                                                                                                    |
| 9   | 14-month waitlist complaint                           | Dr. Voss    | **"You're on the list. Next question."**                                                                                                                          |

### The 5 Resolutions

1. Adopt FY2024 Annual Report — **Passed**
2. Approve Series C terms — **Passed**
3. Ratify appointment of external auditor — **Passed**
4. Authorize international expansion plan — **Passed**
5. **Proposal to Add Push Mode Override (shareholder-submitted)** — **Defeated (3% in favour)**

### Action Items

6 items including:

- _"No action required on Push Mode override proposal — Owner: N/A"_
- _"Publish Appendix G (company holiday schedule) — Owner: Legal & Compliance"_ — Appendix G is referenced in the data request process, the meeting minutes, and elsewhere. It never materializes.

---

## The Annual Report — The 8 Risk Factors

The risk factors are the single best distillation of what RISE is. Each one reads like a legitimate SEC filing while describing something absurd.

1. **Push Mode Regulatory Risk** — inquiries in 3 jurisdictions
2. **Single Mode Dependency Risk** — _"If Push Mode were found to be harmful, restricted, or — least likely — unpopular"_
3. **Audio Data Regulatory Risk** — _"monitoring developments"_ (monitoring their own monitoring)
4. **Autonomous Navigation Incident Risk** — _"incidents have been proportionally small"_
5. **Occupancy Data Sensitivity Risk** — 2,048 sensors at 2.5cm spacing
6. **Waitlist Concentration Risk** — _"If a material portion were to independently develop the capacity to self-initiate morning routines without assistance, revenue projections would be affected. RISE considers the last scenario unlikely."_ — the risk is that people might learn to wake up on their own. RISE considers this unlikely.
7. **Dependency Risk** — _"reduces users' capacity for self-initiated morning routines. RISE considers this an alignment of user behavior with product design intent and not a compensable harm."_ — dependency is a feature, not a bug.
8. **Push Pro Risk** — _"If The Push Pro fails to meet the expectations created by not disclosing its details"_ — the risk of hype generated by saying nothing.

---

## The Security Page — Everything Pending

6 certifications, all pending or in-progress. 8 security features with devastating footnotes. 5 compliance progress bars, all under 30%.

### The August 12, 2024 Pattern

The security page is where the "everything stopped when Arvin left" pattern is most visible:

- Key rotation: _"last completed: August 12, 2024"_ (Arvin's last day)
- Cloud Infrastructure reviewer: _"A. Reyes"_
- SOC 1 Documentation: _"40% complete as of August 2024"_
- Continuous Monitoring: _"The team is aware. The team has been aware."_
- RBAC: _"Access control enforcement layer: Scheduled for implementation. Document visibility default: Public."_
- Incident Response: _"Remaining 9% of incidents have been monitored since Q3 2022. Monitoring continues."_

### Trust Center

`/security/trust-center` — a "Coming Soon" page. Expected launch: **Q4 2024.** Last updated: **August 12, 2024.** It's April 2026. The Trust Center has been "coming soon" for 18 months.

---

## The Legal Documents — The Most Absurd Clauses

Across 6 legal documents totaling ~108 sections, here are the clauses that define the universe:

### Terms of Service

- §1: _"If the product is currently in Push Mode, these Terms apply regardless of whether you have read them. Proceeding through your morning routine constitutes acceptance."_
- §3: _"Users are encouraged to reflect on how many times they have been told."_
- §5: Prohibited uses include _"attempt to locate, install, or enable an off switch"_ and _"placing objects in the base's path with the intent of stopping it"_
- §8: _"Users own the hardware they have purchased. They do not own anything that runs on it."_
- §9: Data license is _"perpetual, worldwide, royalty-free, irrevocable...It survives the user's decision to stop using the product."_
- §10: Physical risks include _"spillage of hot beverages and resulting burns"_ and _"The bed navigates by momentum. Momentum has consequences."_
- Table of contents includes sections titled: **Free Will Acknowledgment** (§20), **The Button** (§21), **Dependency** (§22), **The Off Switch** (§23)

### Privacy Policy

- §3: _"The question of whether a user can accept a policy update while asleep, if Push Mode activates before they have woken, has been reviewed by our legal team. The answer is yes."_
- §5: Biometric estimates _"are not medical-grade. They are, however, retained as if they are."_
- §6: 2,048 pressure sensors, 64×32 grid, 2.5cm spacing. _"This distinction is made. It is logged."_
- §7: Audio pickup radius ~8 meters. 4-second session buffer. Classification criteria proprietary.
- §9: Section title: **"Data We Are Required To Tell You We Collect"**

### Push Mode EULA

- §6: _"Accidental activation is activation. The user's intent at the moment of button contact is not a factor."_ Note: _"The remote's glow is designed to make it findable in darkness, which may conflict with this recommendation."_
- §7: _"Updates will not add an off switch."_
- §8: _"No version of Push Mode has ever had an off switch. No version will ever have an off switch. RISE considers this section complete."_
- §§14–17: Four escalating "Acknowledgment" sections — Iterations 1, 2, 3, then Final

### Sleep & Environmental Data Policy

- §4: Movement taxonomy includes _"interaction categories that apply when multiple occupants are present."_ Proprietary. _"We are required to disclose that the sensor array is capable of distinguishing between different types of occupant interaction."_
- §5: _"RISE acknowledges that the distinction is primarily definitional"_ (monitoring vs. surveillance)
- §6: Relationship Status Inference — infers from proximity, movement correlation, interaction categories, audio
- §7: Primary account holder determined by who pressed PM-1 first. _"It is final. It cannot be changed. It survives account deletion."_
- §8: Audio retained **indefinitely**. Inference data retained **indefinitely** — _"Inaccurate inference data is updated, not deleted, as historical inference data has research value independent of its accuracy."_

### Autonomous Navigation Disclosure

- §3: _"Contact is a feature of navigation, not an error."_
- §5: Solo return commute added in firmware 2.4.0 via OTA. _"Users who did not want the solo return commute feature were not offered an opt-out."_
- §6: Device navigates _"around them where possible and through them where not possible."_
- §7: Traffic detection: 4m range, 0.3s response = 1.2s obstacle response time. Legal status: _"unresolved in most jurisdictions."_
- §8: Elevators: _"Other elevator users are not consulted."_
- §9: Animals: _"Dogs have been observed to interact with the returning device in a variety of ways."_

### General Disclaimer

- §2: Lists all scenarios that have occurred — glass objects, hot beverages, pets, other occupants. _"The current design reflects RISE's considered position on acceptable contact during routing."_
- §3: Bed navigating into a body of water. _"The button does not know where it is."_
- §5: _"dependency on Push Mode resulting in an inability to self-initiate morning routines"_ — listed as not covered
- §6: Liability cap uses RISE Index (proprietary). _"Users with below-median Index scores are, statistically, the users most likely to have incidents. RISE considers this a coincidence."_

---

## Easter Eggs — Complete Catalog

### In the `easter-eggs.tsx` Component

1. **Konami Code** (↑↑↓↓←→←→BA): Applies `grayscale(1)` to the entire page, overlays fractal noise grain at 15% opacity, displays banner: _"Push Mode override requested. Override not available. This is a feature, not a limitation."_ Auto-resets after 2.8 seconds.

2. **Push Listener**: Monitors all `<input>`, `<textarea>`, and `<select>` fields globally. If the user types a value ending in "push", the document title changes to **"Push Mode: Active"** for 2 seconds.

### Scattered Across the Codebase

3. **The Internal Not-Found Link**: `/internal/not-found.tsx` contains a nearly invisible link to `/internal/docs/arvin-final-commit` — 1px font size, 4% opacity, `aria-hidden`, `tabIndex={-1}`, `userSelect: none`. You'd need to inspect element to find it.

4. **The Sitemap Confession**: The HTML sitemap's Internal and Hidden sections are styled in amber with the annotation _"← this section should not be here"_. Bottom text: _"IT has been notified that the Internal section of this sitemap contains routes that should not be publicly indexed. The notification was sent February 12, 2025. This sitemap was generated March 1, 2025. The routes remain listed."_

5. **The robots.txt Essay**: The `robots.ts` file contains a multi-paragraph comment explaining why `/internal/` and `/remote/` are disallowed — not because they're private, but because _"Excluding it from robots.txt does not resolve the access issue but does reduce discoverability."_ RISE considers this an acceptable interim measure.

6. **The 404 Page**: Push Mode takes credit — _"Push Mode navigated here on your behalf. The page was not present. The bed is returning."_ An animated blue line represents the bed returning. Then: _"Push Mode has noted this outcome and will adjust future routing accordingly. This is a feature, not a limitation."_

7. **Multiple Button Presses on /remote**: More than 2 presses during routing produces a 9px italic message at 10% opacity — barely visible, acknowledging your input while ignoring it.

8. **The `beforeunload` Handler on /remote**: During routing, attempting to close the tab triggers a browser warning — _"Push Mode cannot be interrupted once initiated."_

---

## Cross-Reference: Recurring Narrative Anchors

These are details that appear in multiple places and must remain consistent:

### August 12, 2024

This date is RISE's "Day Zero" — the day Arvin left. It appears in:

- Internal system: Last deploy date, days-since counter
- Users page: Arvin's last login (9:43am)
- Settings: Last deployed, deployed by areyes
- Security: Last key rotation, SOC 1 documentation, Trust Center last updated
- Arvin's farewell note: Date of the file
- Press releases: Compliance data release (Aug 14, 2024 — two days after Arvin left)

### Appendix C

Referenced in meeting minutes Q3 ("I can confirm it exists"), annual report (Ellery "has been briefed on Appendix C"), and media contact policy (Voss not available for comment on "Appendix C"). Never explained. Never published.

### Appendix G (Company Holiday Schedule)

Referenced in data request process (processing paused for holidays per "Appendix G — forthcoming"), meeting minutes action items ("Publish Appendix G — Owner: Legal & Compliance"). Never published. Always forthcoming.

### "6:47am"

Dr. Voss's signature time. The Nudge discontinuation memo was written at 6:47am. The shareholder letter was written at 6:47am. This is 47 minutes after her 6:00:00am Push Mode activation.

### "Have a productive day!"

The only exclamation point in the entire RISE brand. Appears on:

- The PM-1 remote's fine print (physical product and `/remote` page)
- Push Mode completion message
- The tagline hierarchy as "Remote Fine Print"

### 98% Compliance

Referenced in: homepage stats, product page, shareholder letter, press page (Bloomberg quote), annual report, meeting minutes. Always stated without context for what the other 2% experienced.

### "This is a feature, not a limitation."

Appears in: Konami code overlay, remote fine print, help FAQ, 404 page, security page, and throughout legal documents. The RISE equivalent of "by design."

### The Off Switch

Referenced across 10+ locations. Terms §23 ("The Off Switch"), EULA §8 ("RISE considers this section complete"), Push Pro notes ("There will not be an off switch"), meeting minutes (override proposal defeated 3%), about page ("0 off switches"), Nudge page ("Yes — this was later reconsidered"), homepage stats ("0 off switches"). The off switch is the most thoroughly documented non-feature in the brand.

### The RISE Index

A proprietary score that affects liability caps (§6 of Disclaimer), is available via DataKit SDK, has a methodology document (DOC-008) that is entirely redacted, was published on April Fools' Day, and Dr. Voss personally redacted her own score.

### "David K." / Dave

The customer avatar canvas (DOC-016) names the target customer "David K." — the same name as Dave, the protagonist of PUSH. This is the film character appearing in the marketing consultant's customer persona. Section 9 was crossed out and rewritten by Dr. Voss.

---

## The Homepage — Key Details

### Testimonials

| Reviewer            | Quote                                                                                              | Stars |
| ------------------- | -------------------------------------------------------------------------------------------------- | ----- |
| K.M., VP Operations | _"I genuinely cannot tell if I like this product. I made VP last quarter."_                        | 4★    |
| D.K., Analyst       | _"I pressed the button thinking it would adjust my back support. I arrived at my desk at 8:47am."_ | 5★    |
| Anonymous, Verified | _"My husband bought one. He's never been late. We don't really talk about it."_                    | 5★    |

"K.M." is Karen from the film. "D.K." is Dave (David K.) from the film.

### Stats Bar

98% on-time · 0 off switches · 4.7★ average · ∞ snooze prevention

### Video Placeholder

A rounded container with play button, corner badges ("RISE" / "Push Mode"), and text: _"'PUSH' — a short film. One morning. One button."_ Subtext: _"Dave did not consent to this film. Dave arrived at work on time. Results typical."_

---

## The Investor Press Page — Selected Quotes

10 fabricated media quotes, each from a real publication, each reflecting that publication's actual editorial voice:

| Publication      | Key Line                                                                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The Atlantic     | RISE includes it _"because we believe in transparency. We also believe our answers are in the documentation, which the Atlantic reporter did not read."_ |
| Wired            | _"I arrived at my desk at 8:47am. I don't know what happened between the bedroom and the elevator."_                                                     |
| Consumer Reports | _"4.7 stars. We cannot fully explain this score."_                                                                                                       |
| The NYT          | _"None of them could explain why they signed up. All of them said they would do it again."_                                                              |
| Bloomberg        | _"98% compliance. This is higher than most medications."_                                                                                                |
| TechCrunch       | _"We asked for an interview with the Push. RISE said the Push does not give interviews. The Push arrived at our office at 8:52am. It stayed until 5pm."_ |
| The Guardian     | _"A bed that won't let you stay. In late capitalism, this passes for innovation. Four stars."_                                                           |

---

## The Help / FAQ Page — All 9 Answers

The FAQ page hero: _"If you are reading this, Push Mode is likely already running."_
Status badge: _"You were referred here from the RISE PM-1 remote."_

All 9 answers are worth preserving:

1. **Can Push Mode be turned off?** _"No...We recommend leaning into it."_
2. **Multiple button presses?** _"Each press confirms your original input...The bed has received your message. It will continue."_
3. **Wrong room?** _"Please check whether the room the bed delivered you to was, in fact, the right room. The bed's navigation has proven correct in 98% of cases where the user believed it to be incorrect."_
4. **Pillow not centered?** _"Please finish getting ready."_
5. **Bed followed me to work?** _"Yes. Most users report finding it reassuring within two to three weeks."_
6. **Stairs?** Full paragraph ending with _"There is no loyalty discount. We appreciate your patience and your purchase."_
7. **Nudge upgrade?** _"We respect the role it played in your mornings and do not offer trade-in credit."_
8. **How to stop Push Mode?** _"You would need to not press the button. We recognize this may be more difficult than it sounds."_
9. **The Push Pro?** _"We are not currently accepting questions about The Push Pro."_

Warranty: Push Mode: **lifetime**. Hardware: 5 years.

---

## Vision 2045 — The Escalation

5 vision versions (1.0–5.0, Q1 2021–Q1 2025). Notable: Vision 2.0 _"Children's product line added, then removed from same document."_

**5-Year (2030):** 2M units, 47 countries, _"Push Mode in Every Bedroom."_ Corporate wellness — _"HR departments are not the audience RISE imagined...They are highly motivated buyers."_ Municipal transit pilot: 34% on-time improvement.

**10-Year (2035):** _"RISE is not a bed company."_ Third-party integrations with coffee makers, smart homes. _"The bed knows your first meeting. It knows the traffic."_

**20-Year (2045):** Global morning infrastructure.

---

## Unbuilt / Planned Pages

These were discussed in conversation but never implemented:

| Page                    | Description                           | Status                               |
| ----------------------- | ------------------------------------- | ------------------------------------ |
| `/institute`            | RISE Sleep Science Institute          | Not built                            |
| `/trust`                | Trust/Security center (expanded)      | trust-center exists as "Coming Soon" |
| Changelog               | 18 entries + tombstone                | **Not found in current codebase**    |
| Status page             | Service status dashboard              | **Not found in current codebase**    |
| Careers                 | 6 job postings                        | **Not found in current codebase**    |
| Enterprise              | Enterprise sales page                 | **Not found in current codebase**    |
| `/index-score`          | RISE Index estimator                  | Not built                            |
| Compliance calculator   | Interactive calculator                | Not built                            |
| Referral dead-end       | Referral flow that leads nowhere      | Not built                            |
| Community/Forum         | Community page                        | Not built                            |
| Accessibility statement | —                                     | Not built                            |
| Reviews (Supabase)      | User reviews with Drizzle ORM         | Specced, not built                   |
| OG images               | Social media preview images           | Not built                            |
| Spotify playlists       | MCP-generated playlists               | Script exists, not executed          |
| Light mode CSS          | Full light mode polish                | Not done                             |
| Blog rebranding         | Replace Radiant placeholder in Sanity | Not done                             |

**Note:** The conversation summary referenced changelog, status, careers, and enterprise pages as "completed" with specific content, but these do not exist in the current codebase. Either they were discussed/designed but not committed, or they exist in a branch that wasn't merged. The current `ai/chore/remove-trademark-symbols` branch and `main` should be checked.

---

## The Master Timeline — Canonical Chronology

| Date             | Event                                                                                                                                                      | Source                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 2009             | RISE founded by Dr. Eleanor Voss                                                                                                                           | About page                     |
| 2011             | RISE Ambient + RISE Tone (first products, both fail)                                                                                                       | About page, Product Graveyard  |
| 2012             | Thermal, Gradient, Alarm (all fail — users adapt)                                                                                                          | About page                     |
| 2013             | NudgeSense, NudgeLight (app 4.8★, product 2.1★)                                                                                                            | About page                     |
| 2014             | NudgeWarm, NudgeTone (+23 min sleep — made it worse)                                                                                                       | About page                     |
| 2015             | NudgeEdge (lateral tilt — 100% rolled back)                                                                                                                | About page                     |
| 2016             | NudgeBar (74% compliance — cult following)                                                                                                                 | About page                     |
| Nov 14, 2018     | Nudge discontinuation memo (DOC-002) — written at 6:47am                                                                                                   | Internal docs                  |
| 2019             | RISE Nudge (RN-01) consolidated line, later discontinued                                                                                                   | Product page                   |
| FY2020           | Revenue: $2.1M, 940 units, 12% margin                                                                                                                      | Financials                     |
| Q1 2021          | Vision 1.0 written                                                                                                                                         | Vision page                    |
| Jan 3, 2021      | Dr. Voss's Push configured — Unit RSB-0000000000000001                                                                                                     | DOC-003                        |
| Jan 4, 2021      | Voss's first on-time meeting (7:47am) — "She was there before the meeting existed"                                                                         | DOC-003                        |
| 2021             | The Push launches. Revenue: $8.4M (+300%), 3,800 units                                                                                                     | Financials, Shareholder Letter |
| Mar 14, 2022     | SC-0047 — The Coffee Shop (Valencia St, SF)                                                                                                                | DOC-007                        |
| Apr 1, 2022      | DOC-008 — RISE Index Methodology published (April Fools' Day)                                                                                              | Internal docs                  |
| FY2022           | Revenue: $23.7M (+182%), 10,600 units                                                                                                                      | Financials                     |
| Mar 15, 2023     | DOC-006 — HR Workplace Waiver created (still "Awaiting Legal Review")                                                                                      | Internal docs                  |
| Sep–Nov 2023     | Marketing consultant produces DOC-010 through DOC-019                                                                                                      | Internal docs                  |
| Sep 3, 2023      | SC-0089 — The Street Fair (Hayes Valley, SF)                                                                                                               | DOC-007                        |
| FY2023           | Revenue: $38.2M (+61%), 17,100 units                                                                                                                       | Financials                     |
| Jan 9, 2024      | DOC-019 — Retroactive proof of concept for a product on market since 2021                                                                                  | Internal docs                  |
| Feb 8, 2024      | SC-0112 — The Dog (Noe Valley, SF)                                                                                                                         | DOC-007                        |
| Aug 12, 2024     | **Arvin Reyes's last day.** Last deploy. Last login (9:43am). Last key rotation. Last SOC 1 update. Last Trust Center update. Session token: still active. | Everything                     |
| Aug 14, 2024     | Press release: 98% compliance rate (2 days after Arvin left)                                                                                               | Press page                     |
| Oct 22, 2024     | SC-0134 — The Parking Ticket (SOMA, SF) — "unattended motorized mattress of unknown origin"                                                                | DOC-007                        |
| Nov 8, 2024      | Series C: $120M                                                                                                                                            | Press page, Financials         |
| Jan 15, 2025     | DOC-001 — Q4 2024 Incident Log compiled                                                                                                                    | Internal docs                  |
| Feb 1, 2025      | DOC-009 — Audio Data Access Log Q1 2025                                                                                                                    | Internal docs                  |
| Feb 3, 2025      | RISE Move press release — "We are aware of the stairs"                                                                                                     | Press page                     |
| Feb 12, 2025     | IT notified about sitemap containing internal routes                                                                                                       | Sitemap footer                 |
| Mar 1, 2025      | Sitemap generated (internal routes still listed)                                                                                                           | Sitemap                        |
| Mar 1, 2025      | Dr. Voss's shareholder letter — written at 6:47am                                                                                                          | Shareholder Letter             |
| Mar 1, 2025      | DOC-005 — Move Engineering Status (stair navigation RED)                                                                                                   | Internal docs                  |
| Mar 14, 2025     | AGM: 10:04am–2:31pm. Override proposal defeated (3%). "Yes. Next question."                                                                                | Meeting Minutes                |
| Apr 2025         | S-1 filed                                                                                                                                                  | Financials                     |
| FY2024           | Revenue: $89.4M (+134%), 47,000 units, 68% margin, 340K waitlist                                                                                           | Financials                     |
| Q3 2026 (target) | IPO                                                                                                                                                        | Financials                     |

---

## The Unspoken Rules — What Makes It Work

These are the meta-principles that govern the fiction. They are never stated in the website but must be followed by anyone contributing:

1. **Nobody at RISE thinks anything is wrong.** Every document, every FAQ answer, every legal clause is written by someone who believes they are doing excellent, responsible work. The comedy is structural, never vocal.

2. **The bed always works.** There are no malfunctions. Every "incident" is the system operating correctly in an unexpected context. INC-2415: the bed was right, the user's calendar was wrong.

3. **Arvin is sympathetic.** He's not incompetent — he's a junior dev who ran out of time and whose manager didn't ask the right questions. His farewell note is genuine. He liked the job. The Push helped him get up. His auth middleware was "mostly there."

4. **Dr. Voss is not a villain.** She is an extremely competent founder who has never been late since 2021 and who genuinely believes the product improves lives. Her Resistance Index is 0.2 out of 10. She doesn't need the bed — she agrees with it.

5. **James Park is doing his job.** Every legal document is thorough, accurate, and defensive. He's a good lawyer. The fact that the product he's defending is absurd is not his problem. He confirmed Appendix C exists. Next question.

6. **Every number is consistent.** 98% compliance, 340K waitlist, $89.4M revenue, 47,000 units, 2,048 sensors, 64×32 grid, 8-meter audio pickup, 4-second buffer — these numbers appear in multiple places and must never contradict.

7. **Time moves.** The `daysSinceArvin()` counter, the dynamic login times, the "always recent" external IP timestamps — these make the system feel alive. The fiction is happening right now.

8. **Absence is content.** The redacted RISE Index methodology, the unbuilt auth middleware, the empty media library, the reverting settings — what doesn't work tells the story as much as what does.

9. **The exclamation point matters.** "Have a productive day!" is the only one. It appears on the remote's fine print. Its warmth, in context, is the most unsettling thing on the entire site.

10. **The bed has more agency than the user.** It navigates, it commutes, it waits, it returns. It makes itself. It follows you to work. It was correct 98% of the time when the user believed it was incorrect. The bed is the real protagonist — of the product, the film, and the website.
