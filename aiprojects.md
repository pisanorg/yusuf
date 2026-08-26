---
layout: default
title: Adventures in AI
page_class: page-aiprojects
---

<div class="intro-text">
My PhD (Northwestern, 1998) was in AI &mdash; qualitative reasoning and diagrammatic problem-solving, what is now called GOFAI. I built a system that solved 150 problems from a university-level thermodynamics textbook.

Today's AI is a different beast: statistical models, billions of parameters, and the ability to hold a conversation and write production code. I started building with Claude, Gemini, ChatGPT, and GitHub Copilot in March 2026. Everything below was built with significant AI assistance, in reverse chronological order.
</div>

### [Code Analogy Forge](https://code-analogy-forge.netlify.app)

Paste a code snippet or just type "recursion", pick your audience (curious child, high school student, CS undergrad, non-technical adult), and get three analogies from three different everyday domains, each with a small table mapping code terms to the analogy. Switching the audience swaps the entire text, not just the vocabulary: the child hears about a present that is a box inside a box inside a box, the undergrad gets the same imagery tied to base cases, unwinding, and stack frames. A detector works out what your paste shows from keyword mentions and code shapes (lo/hi/mid bounds for binary search, .push() plus .pop() for a stack), and for recursion it extracts the actual function body, by brace matching or Python indentation, to check the function really calls itself. Save the good ones to a library with tags and search, copy any card as Markdown for slides, or send a read-only share link that needs no server: the link encodes ids into the URL hash and resolves against the corpus shipped with the app.

The idea called for Claude to write the analogies and Supabase to store them. I wrote the analogies up front instead: 25 concepts times 3 domains times 4 audiences is 300 short texts, every mapping checked by a person, same input same output, offline, free. localStorage replaces Supabase. The limitation is the flip side of the corpus: the forge knows exactly 25 concepts (variables through closures, threads, encryption, and graphs), and anything outside them gets an honest "no known concept detected" rather than a fresh analogy. The original pitch wanted the open-ended tail, and that part really did need the LLM. 97 vitest tests, 99.9% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/code-analogy-forge/README.md) for more details on the code or try it at <https://code-analogy-forge.netlify.app>

(Last update August 2026)

### [HAR Detective](https://har-detective.netlify.app)

Export a HAR file from the DevTools Network panel (right-click, "Save all as HAR"), drop it on the page, and get the analysis you normally do by squinting at a wall of requests: an interactive waterfall plus a ranked list of what is actually wrong. Ten detectors cover the classics: N+1 loops (/api/products/1 through /8 becomes one finding with the batch-endpoint fix attached), static assets served without cache headers, hundreds of KB of JSON that never met gzip, redirect chains, API calls running single-file when they could run together, duplicate fetches, failing requests, slow server think-time, oversized payloads, and HTTP/1.1 origins paying DNS and TLS over and over. Each finding shows the guilty requests, the wasted bytes or milliseconds, and a copy-paste fix; click one and the rows light up in the waterfall. The whole report exports as Markdown for a PR.

The idea called for Claude to read the request data and write the report. HTTP performance problems are a small, well-known catalogue, so hand-written rules do the job: same HAR, same report, offline, and the file never leaves the browser (HAR exports are stuffed with cookies and session tokens, so this matters more than usual). The limitation is that rules judge shape, not intent: a detector can see that three API calls ran strictly one after another, but not that your app needed the first response to build the second request, so some findings are the app working as designed. It flags; you decide. 56 vitest tests, 100% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/har-detective/README.md) for more details on the code or try it at <https://har-detective.netlify.app>

(Last update August 2026)

### [Claude for STEM Professors](https://github.com/pisanuw/claude-for-stem-professors)

A guide for faculty who have seen the demos and want to ship something: from zero to a deployed course app, no programming background required. The bet behind it is that the hard part for professors is not prompting, it is plumbing. So the first half is accounts, tokens, and connectors (GitHub, Netlify, Render, Canvas), and only then come three destination projects with paste-ready starter prompts: a course website live on Netlify in under an hour, an auto-graded practice-problem app students use before exams, and a Canvas assistant on Render that drafts announcements from live roster and assignment data.

Two things I insisted on. The guide is dated, not evergreen: everything was verified against vendor documentation in August 2026, the version sits at the top, and when a button wanders, the linked docs win. And token hygiene is a full section rather than a footnote, written from experience: tokens are passwords, a Canvas token carries FERPA-protected student data, and every paste-a-token session ends with rotate or delete. Every starter prompt closes with "Ask me any questions before you start", the guide's single highest-value habit, because Claude's guesses are plausible and wrong in exactly the ways that waste your afternoon. Ships as one README plus a printable PDF (pandoc and weasyprint) with the URLs spelled out for reading away from a screen.

See [README](https://github.com/pisanuw/claude-for-stem-professors/blob/main/README.md) to get started; the printable PDF is in the repo.

(Last update August 2026)

### [SQL Replay](https://sql-replay.netlify.app)

Type a SELECT, paste some CSV (or use the bundled customers/orders tables), and watch the query execute one stage at a time: FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY, LIMIT. Every stage shows the actual rows: joined rows merge with their partners, LEFT JOIN survivors get NULL padding, rows that fail WHERE are struck through with the evaluated condition sitting next to them, groups collapse with their member lists. A narrator explains each stage from the real execution counts ("3 rows pass, while 2 rows fail and are removed"). Students pick up SQL syntax in a week and then spend a quarter with no mental model of what the database does with it. Watching the rows move is the model. The whole workspace, query plus data, is encoded into the URL hash, so a puzzle query goes to a class as a plain link.

The idea suggested an optional Claude API narrator. I made it the mandatory non-Claude narrator instead: every sentence is a template filled with numbers the executor just computed, so the explanation cannot drift from the screen, and the semantics underneath are the real thing (three-valued logic, Kleene AND/OR, COUNT(x) skipping NULLs, inclusive BETWEEN). The limitation is the point: it replays the logical clause order on tables capped at 200 rows, with no planner, no indexes, and no subqueries. A real engine would almost never execute a query this literally, so this teaches what a query means, not how a database makes it fast. 86 vitest tests, 99.7% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/sql-replay/README.md) for more details on the code or try it at <https://sql-replay.netlify.app>

(Last update August 2026)

### [Sound Sketchpad](https://sound-sketchpad.netlify.app)

Type "muffled explosion heard from underground" and it plays one. The description runs through a word-to-DSP recipe book: 20 base sounds (explosion, coin, laser, rain, bell, heartbeat) and 18 modifiers (muffled, tiny, metallic, underwater, retro), each modifier rewriting the recipe by re-filtering, re-pitching, or bolting on ringing partials. The app shows exactly which words matched, draws the waveform, lists every layer's signal chain (oscillator to filter to envelope to gain), and gives you sliders for pitch, length, brightness, echo, and volume. One button exports a WAV at 16 or 24 bit. Same words, same sound, every time; a Variation button re-rolls only the noise seed.

The idea called for Claude to turn the description into Web Audio code. I replaced it with the recipe book, and skipped Web Audio for synthesis too: a pure sample-by-sample DSP engine (swept oscillators, seeded noise, ADSR envelopes, biquad filters, echo, bit crush) renders the exact buffer the browser plays, which means the tests assert on the actual samples you hear and the WAV export is a byte-for-byte re-render. The limitation is the vocabulary: 20 bases and 18 modifiers cover the game-jam staples, but describe anything outside them and you get a generic whoosh and a hint about words that work. The open-ended tail really did need the LLM. 59 vitest tests, 100% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/sound-sketchpad/README.md) for more details on the code or try it at <https://sound-sketchpad.netlify.app>

(Last update August 2026)

### [Code Review Gauntlet](https://code-review-gauntlet.netlify.app)

A code snippet appears with one to three planted defects and a countdown. Click the lines you would flag in review, submit, and everything is revealed: the off-by-one you caught, the SQL injection you sailed past, each with its root cause and fix. Scoring punishes spraying: 100 points per defect found, minus 25 for every clean line flagged, and the time bonus only pays out when you found them all. A radar chart tracks accuracy across logic, null-safety, security, performance, and style, so after a dozen rounds you can see which category you keep missing. There is also a daily challenge: the date is hashed into the puzzle seed, so everyone gets the same round with no server behind it.

The idea called for Claude to generate endless fresh puzzles and Supabase for a leaderboard. I skipped both. Puzzles come from a seeded mutation engine: 11 hand-written clean snippets (JavaScript, Python, SQL) and a catalogue of 51 single-line defects, from inverted guards to timing-unsafe hash comparisons, each rewriting exactly one line so the generated code always parses. Same seed, same puzzle, offline, free. The honest limitation is the flip side: 51 defects is not an infinite supply, and a regular player will start recognizing templates within a week or two. The original pitch really did need an LLM for that part. 46 vitest tests, 99.8% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/code-review-gauntlet/README.md) for more details on the code or play it at <https://code-review-gauntlet.netlify.app>

(Last update August 2026)

### [UI Diff Lens](https://ui-diff-lens.netlify.app)

Drop in before and after screenshots of a UI and every changed region gets boxed and named: layout shift, spacing nudge, color restyle, text edit, visibility fade, added, or removed. Each box carries a confidence and the actual evidence ("the same content reappears 8px right, match 100%"). Pixel-diff tools already tell you where pixels differ; the useful part is naming the kind of change, so a reviewer can wave through nine color tweaks and stare hard at the one layout shift. Filter the overlay by type, then export an annotated PNG or a standalone HTML report for the PR.

The idea called for Claude Vision to do the classifying. It turned out to be classical image processing all the way down: a perceptual pixel diff with anti-aliasing detection finds the changes, clustering groups them into regions, and each region runs a gauntlet of checks (is one side just background, does the content reappear at an offset within 48px, is one side an alpha-blend of the other, do the edges correlate while the palette moved). Deterministic, offline, and screenshots never leave the browser. Heuristics have edges, though: a wide element nudged a few pixels produces two thin changed strips, and if they land far enough apart the tool reports an add plus a remove instead of one spacing change. 56 vitest tests, 96% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/ui-diff-lens/README.md) for more details on the code or try it at <https://ui-diff-lens.netlify.app>

(Last update August 2026)

### [Shortcut Sprint](https://shortcut-sprint.netlify.app)

A flashcard app for your fingers. It shows a task ("Go to definition", "delete the current line"), you press the shortcut, and SM-2 spaced repetition (the SuperMemo algorithm from 1990, same family as Anki) decides when you see that card again: instant recall pushes it out days, then weeks; fumbling brings it back tomorrow. VS Code, Chrome DevTools, Figma, and Vim come bundled, including multi-chord sequences like Ctrl+K Ctrl+S and Vim's ciw, and instructors can upload a JSON set for whatever tool their course uses. A per-tool mastery radar and a daily streak provide just enough guilt to keep the habit going.

The idea called for Supabase to hold progress. I skipped it: localStorage does the job, so there are no accounts and nothing leaves the browser. The matching layer turned out to be the interesting part, because a keypress has two readings (the physical key and the character it produced) and Vim's $ needs one while Ctrl+Shift+[ needs the other, so every press is matched both ways. The limitation is baked into the platform: a web page cannot capture browser-reserved shortcuts, Ctrl+W closes the tab no matter how much preventDefault you throw at it, so the one shortcut everyone knows is the one this app cannot teach. 78 vitest tests, 98% coverage, no backend, no API keys.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/shortcut-sprint/README.md) for more details on the code or try it at <https://shortcut-sprint.netlify.app>

(Last update August 2026)

### [Migration Diff Narrator](https://migration-diff-narrator.netlify.app)

Paste two versions of a database schema, or two versions of your TypeScript interfaces, and get every change named and judged: safe, caution, or breaking, each with a one-sentence migration note ("Existing NULLs make this fail; backfill the column before adding the constraint"). Renames are inferred instead of being reported as a drop plus an add, so `user_name` becoming `username` shows up as a rename warning rather than a data-losing delete. One button copies the whole thing as a Markdown checklist ready for a PR description. Schema changes are the most dangerous part of a deploy, and the diff between two migration files is usually raw SQL a reviewer has to simulate in their head. This turns that into a ten-second scan.

The project idea called for the Claude API to classify each change. I skipped it. The taxonomy of schema changes is small and enumerable, so a fixed rule set does the job: same diff, same verdict, every time, offline, nothing you paste leaves the page. The honest limitation is parser coverage: it reads the common subset of SQL DDL (CREATE TABLE, ALTER, indexes, enums) and object-shape TypeScript interfaces, not every dialect corner, and it warns you when it skips something it does not understand. 74 vitest tests, no backend, no API key.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/migration-diff-narrator/README.md) for more details on the code or try it at <https://migration-diff-narrator.netlify.app>

(Last update August 2026)

### [Schema Storyteller](https://schema-storyteller.netlify.app)

Point it at a schema (SQL DDL, Prisma, or JSON Schema) and it tells you the story: which entities exist, how they relate, which tables are just join tables, and what `usr_actv_flg` was probably meant to say. A rule-based reviewer then lists what is likely missing: primary keys, indexes on foreign keys, uniqueness constraints. Export the whole narrative as Markdown and paste it into the design doc that should have existed in the first place.

No LLM here either, on purpose. A hand-written parser and a fixed rule set replace the suggested Claude API calls, so the narrative is free, offline, and reproducible, which also means it is templated: the prose will not win any literary awards, and the reviewer only knows the rules I taught it. 71 vitest tests, 88% coverage, fully client-side.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/schema-storyteller/README.md) for more details on the code or try it at <https://schema-storyteller.netlify.app>

(Last update August 2026)

### [Pathfinding Playground](https://pathfinding-playground-pisanuw.netlify.app)

Draw a grid map, drop in walls and mud (mud costs 5 to enter), then watch A*, Dijkstra, BFS, DFS, and greedy best-first think one expansion at a time, each step narrated from the live algorithm state: which cell got picked, why, and what the g, h, and f values were. The project idea suggested Claude API calls for the narration. I skipped that. Every line is a template filled with the numbers the algorithm just computed, so narration is free, instant, works offline, and always matches what the search actually did, which an LLM cannot promise.

Each algorithm is a generator emitting a uniform event trace, and the canvas renderer and the narrator both consume the same events, so what you see and what you read cannot drift apart. Neighbor order and tie-breaking are fixed, so the same map always produces the identical trace; there is a test for that. The classroom payoff is compare mode plus share links: sprinkle mud, run BFS against Dijkstra side by side, watch BFS march straight through the expensive terrain while Dijkstra detours around it, then hand the exact puzzle to a class as a plain link, because the whole map, start, goal, and algorithm picks are run-length encoded into the URL hash. React + Vite, no backend, 20 vitest cases covering optimality, path validity, maze solvability, and trace determinism.

See [README](https://github.com/pisanuw/pathfinding-playground/blob/main/README.md) for more details on the code or play it at <https://pathfinding-playground-pisanuw.netlify.app>

(Last update August 2026)

### [Game Palette Inspector](https://game-palette-inspector.netlify.app)

Check a game palette against WCAG contrast and eight kinds of color vision deficiency, then get replacement colors that keep the art style. Roughly 8% of male players see color differently, and most game color tooling ignores them. Build a palette by hand, load a preset, or drop a screenshot and have its eight dominant colors pulled out; the vision lab then shows the palette, and the full frame, through protanopia, deuteranopia, tritanopia, their milder forms, and full and partial achromatopsia.

Two parts I like. The confusion report measures color pairs perceptually in OKLab and flags the ones that are clearly distinct with typical vision but collapse under a specific deficiency, naming the worst-case vision type. And the fix studio repairs a failing color by binary-searching OKLCH lightness with hue pinned, so the contrast target is met without repainting the art direction. It is also honest about impossibility: 7:1 against a mid-tone background is sometimes unreachable, and the tool says so instead of inventing a color. The simulation is Machado, Oliveira and Fernandes (2009), applied in linear sRGB and verified against the colour-science reference data. Everything runs in the browser: no accounts, no uploads, no tracking, no runtime dependencies beyond React, all the color math hand-rolled and unit tested. The interface follows its own advice, too: the accent is a protan/deutan-safe cyan and no pass/fail state is carried by color alone. Simulations are good approximations, not ground truth; individual perception varies.

See [README](https://github.com/pisanuw/c1/blob/main/README.md) for more details on the code or use it at <https://game-palette-inspector.netlify.app>

(Last update August 2026)

### [Google Flights MCP Server](https://github.com/pisanuw/claude-google-flights-mcp)

An MCP server that hands Claude nine tools for searching flights and watching fares. Google has no official flights API, so this calls SerpAPI's `google_flights` engine, which runs the search server-side and returns structured JSON. You can search one-way, round-trip, or multi-city, filter on cabin class, passengers, stops, and price, follow a `departure_token` to advance leg by leg through an itinerary, and follow a `booking_token` to see which providers sell the fare and at what price. "Nonstop round-trip SEA to NRT, Oct 3 back Oct 17, under $1200" is the whole interface.

The part I actually use is the price watching. Save a search as a watch with an optional target, and `check_prices` re-runs every watch, records what it finds, and reports drops and target hits, with a full price history per watch. A standalone checker script can be put on a schedule for hands-off alerts that fire a native macOS notification. Around 900 lines of Python, no build step, registers with Claude Code in a single command.

Honest limitation: this is scraping as a service, so it inherits SerpAPI's rate limits (the free tier is 100 searches a month) and whatever Google changes about its result pages.

See [README](https://github.com/pisanuw/claude-google-flights-mcp/blob/main/README.md) for setup

(Last update August 2026)

### [Teaching an LLM Tutor to Withhold the Answer](https://arxiv.org/abs/2608.12292)

A paper on the engineering problem behind the Socratic guardrail: a capable model asked nicely, or asked angrily, will not reliably refuse to give an answer it could easily produce. A prompt is not enough. So the tutor enforces answer-withholding as a per-turn, machine-checkable contract instead. A non-LLM policy core reads only trusted learner state and sets a ceiling on an eight-rung help ladder, a deterministic detector strips solution code, and a separate LLM judge checks each risky reply against the contract before it is sent.

The tuning method may be the more portable contribution. Scripted student personas are driven through the live pipeline and re-scored by a stronger model, with every rejection's stated reason recorded, so failures get fixed by cause rather than by vibes and no human subjects are needed to iterate. That surfaced an "over-help ladder" that I did not expect to be so orderly: fix the blatant solution leaks and the tutor starts naming the exact bug; fix that and it starts over-citing general facts. Each fix exposes the next rung. The measure, diagnose, and fix loop generalizes to any agent that has to refuse a capability it has.

Claude was a heavy collaborator on this one, which is a slightly recursive situation: a language model helping write up how to stop a language model from being too helpful.

Read it at <https://arxiv.org/abs/2608.12292>

(Last update August 2026)

### [Teaching Intro AI When the Tools Can Do the Homework](https://arxiv.org/abs/2608.05175)

An experience report on redesigning CSS 382, our intro AI course, once it became clear that a language model could complete most of the assignments in it. The response was not to freeze the curriculum. The classical core stayed (search, adversarial search, MDPs, reinforcement learning) and a strand was added in which students build a language model from scratch, so that a tool they are required to use is also one they are required to understand. Assessment moved to work that resists unattributed automation: in-class exercises, reflective writing, and a defended team project. Examinations were removed entirely. The AI policy went from unmentioned in 2023 to required in 2026.

The center of the paper is the part I did not plan for. The cohort deliberated on and ratified a Student Bill of AI Rights governing *my* use of AI, including a provision that I personally complete any AI-generated assignment before issuing it. The prompt that scaffolded their deliberation was itself AI-generated, and the paper treats that provenance as part of the story rather than a footnote. It also reports the tensions, including students objecting to AI-generated course materials, and is explicit about how little a single-cohort design narrative can actually claim.

Read it at <https://arxiv.org/abs/2608.05175>

(Last update August 2026)

### [How of Happiness Quizzes](https://how-of-happiness.netlify.app/)

Ten chapter quizzes, twenty questions each, with Google sign-in and a leaderboard. React and Vite on the front, Supabase (Postgres, Auth, row-level security) on the back, Netlify for hosting.

Two design decisions carry the whole thing. First, your chapter score is the average of every attempt, not your best, which makes retakes free to take but not free to fail: open with 15 out of 20 and you are capped at 18.3 after three attempts and 19.5 after ten, approaching a perfect score without ever arriving. One bad attempt is permanent. Only a perfect first attempt scores perfectly. The global board sums your chapter averages, so breadth pays and every chapter you play can only add to your total. Second, players show as initials with no photo by default, because signing in with Google should not publish your full name and face to a public page. That default is enforced in the database rather than the interface: the leaderboard view returns a photo only when the player opted in, the profiles table is readable only by its owner, and players hold update rights on exactly two columns, so nobody can point their avatar at an arbitrary image.

Questions live in JSON, one file per chapter, with a seed script that validates before it writes.

See [README](https://github.com/pisanuw/quiz/blob/main/README.md) for more details on the code or play it at <https://how-of-happiness.netlify.app/>

(Last update August 2026)

### [Building with AI: a mini workshop](https://mini-ai-app-workshop.netlify.app)

A one-hour hands-on session that takes complete beginners from "AI is a mystery" to a working web app they built by describing it. Not a lecture about AI, and no code shown: the participants each end the hour with something on a screen that they made.

The repo is the whole kit rather than just the slides. A self-contained HTML deck, a participant handout with the prompt recipe, an easy/medium/hard menu of app ideas and ready-to-paste starter prompts, a list of a hundred small app ideas, and a facilitator guide with minute-by-minute timing, the live-demo script, rescue prompts for when someone is stuck, and troubleshooting. The handout is also translated into Turkish. Anyone can pick this up and run the session; that was the point of writing the facilitator guide rather than keeping the timing in my head.

Run it yourself from <https://mini-ai-app-workshop.netlify.app>

(Last update July 2026)

### [LTMS: A Truth Maintenance System in Python](https://github.com/pisanuw/ltms)

A logic-based Truth Maintenance System and pattern-directed reasoning engine in pure Python, following Forbus and de Kleer's *Building Problem Solvers* (MIT Press, 1993). The system maintains belief across a set of propositional clauses using Boolean Constraint Propagation, records well-founded support for every derived value, backtracks in a dependency-directed way when it hits a contradiction, and can explain why it believes anything it believes. Assert `p or q`, then assert `not p`, and it concludes `q`. Assume it is raining and it will conclude the ground is wet; retract the assumption and the wet ground goes back to unknown rather than lingering as an orphaned conclusion. That retraction behavior is the entire point of a TMS, and it is what separates it from a rule engine that only ever adds.

The reason to build it: JTMS and ATMS have a few toy ports, but the clausal-BCP LTMS with dependency-directed backtracking is close to unported outside Lisp and Racket. This is a clean, typed, tested version, roughly 6,300 lines across 16 modules, 143 tests, published on PyPI as `ltms` 0.1.0 under MIT. It goes past the base implementation into indirect proof, closed-world assumptions, dependency-directed search, prime implicates for logical completeness, and a SAT-style two-watched-literals BCP engine, with differential tests against PySAT. World models can live in `.kb` data files instead of Python, and those files carry `expect` lines that self-check when the file runs.

Alongside the code is a [documentation site](https://pisanuw.github.io/ltms/) with a 17-chapter study companion walking through the concepts, the runnable examples, and worked solutions to the book's exercises. The book itself comes from the Qualitative Reasoning Group at Northwestern, which is where my own qualitative-reasoning PhD came from, so this is partly a thirty-year round trip: the algorithms I learned in Lisp, rebuilt in Python with a language model as the pair programmer.

Still missing: a deployed site where you can type in rules and facts and watch belief change, retract an assumption, and ask the system why. That is the next piece.

See [README](https://github.com/pisanuw/ltms/blob/main/README.md) for more details on the code, or read the [study companion](https://pisanuw.github.io/ltms/)

(Last update August 2026)

### [Ladder Games](https://word-path.netlify.app/)

Two puzzle games in one app, sharing a structure and a stubborn design principle. **Word Ladder** asks you to change one letter at a time to climb from a start word to a target, scored on how close your path came to the shortest one. **Number Ladder** gives you a set of numbers and the operators `+ − × ÷ ^` and asks you to hit a target, Countdown-style, using each number at most once. Both offer Free Play and a Climb Mode that keeps raising the difficulty until you decide to stop.

The dictionaries are the interesting part of the word game: 26,419 entries across English words, Turkish words, English names, and Turkish names, at lengths 3 through 7. Each file holds only the largest connected component of the one-letter-change graph for that category and length, so puzzle generation is structurally incapable of handing out an unsolvable pair. The math side has the mirror-image guarantee: a memoized solver searches every reachable set of remaining numbers, both to verify a generated puzzle has a good solution and to show you the best possible result next to your own afterwards. The operator rules are deliberately unambiguous (subtraction is always `|a − b|`, division is always larger over smaller and only when it divides evenly) so a correct idea never fails on move order. UI is bilingual, English and Turkish.

The Hint button is the Socratic guardrail in miniature. Word Ladder tells you which letter position to change, never what to change it to. Number Ladder highlights which two numbers to combine, never the operator or the result. Each hint costs a flat 10 points off the round, so hint use limits itself without needing a cap. React + Vite, no backend required to play; an optional Supabase table adds a public leaderboard that records hints used alongside the score.

See [README](https://github.com/pisanuw/word-path/blob/main/README.md) for more details on the code or play it at <https://word-path.netlify.app/>

(Last update August 2026)

### [Computing Power and Political Power](https://pisanuw.github.io/turkey-study-abroad/)

A UW faculty-led study abroad program in development for Winter 2028, co-directed with Asli Cansunar (Political Science, UW Seattle). Around twenty students spend the quarter in Istanbul taking three co-taught courses that pair a technical skill with a political-economic question: The Technology of Resistance (censorship, throttling, VPNs and Tor, measured with OONI, against the political science of networked collective action), Computational Political Economy of Turkey (OCR, geocoding, and choropleth mapping applied to Ottoman and Republican-era registers to see where public goods actually went), and a Fieldwork Practicum where mixed teams carry one applied project from question to public presentation. Computing students get the political economy, political science students get the command line, and every student does both. The site is four static pages on GitHub Pages with the three draft syllabi, the ten-week arcs, and a shared excursion week in Izmir and Ephesus.

The program is not an AI project, but it is an AI artifact: the site and the draft syllabi were written with Claude. The program still has to be reviewed by both instructors and confirmed by UW Study Abroad, so everything on the site is labeled a working draft and nothing is open for applications yet.

Read the drafts at <https://pisanuw.github.io/turkey-study-abroad/>

(Last update August 2026)

### [Emoji Lingua](https://emoji-lingua-pisan.netlify.app)

Translate English into emoji, and emoji back into English. `I love pizza on a rainy night` becomes 👤 ❤️ 🍕 🔛 🌧️ 🌙; unknown words stay in place rather than disappearing, and a hint under the result tells you how many there were. The dictionary has 18,474 word-to-emoji entries (1,535 of them multi-word phrases) and 4,218 emoji-to-word glosses, generated from the Unicode CLDR annotations and then layered with hand-authored vocabulary: composed entries for abstractions (`democracy` → 🗳️, `justice` → ⚖️), function words that get dropped so the output reads cleanly, and curated overrides so the obvious choice wins (`cat` → 🐱, not 🐈). Phrases match greedily longest-first, so `good morning` → 🌅 rather than 👍 🌅, and a suffix-rule fallback catches forms the generator never materialized. The engine is hybrid: the dictionary is deterministic and always available, while Claude (when an API key is configured) handles context and can read an emoji sequence as a sentence instead of a word list. The AI path always degrades to the dictionary on any error, and the UI labels which engine produced each result, so a model outage cannot break the app. Express server wrapped as a Netlify serverless function, static page on the CDN, 44 tests at ~94% statement coverage. Honest limitation: emoji to English is a gloss, not grammar, so 🐱🍕 gives you `cat pizza`, not `the cat ate pizza`.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/emoji-lingua/README.md) for more details on the code or use it at <https://emoji-lingua-pisan.netlify.app>

(Last update August 2026)

### [Canvas Group Evaluate](https://github.com/pisanuw/canvas-group-evaluate)

A command-line tool that generates a ready-to-deploy Google Form for peer and self evaluations from a Canvas group set. Two Python scripts do all the work: `fetch_roster.py` pulls groups and students from the Canvas API (or reads a CSV/TXT file you supply) and writes `roster.json`; `generate_apps_script.py` turns that into a self-contained Apps Script file you paste into script.google.com and run once. The resulting form uses section navigation to route each student to their own group's rubric, with a configurable Likert block (Technical Contribution, Reliability, Communication, Problem Solving) plus two open-text questions per member. The form is locked to your Google Workspace domain (e.g. `@uw.edu`) so only signed-in students can respond. No web deployment — runs locally whenever the instructor needs to generate a new evaluation form.

See [README](https://github.com/pisanuw/canvas-group-evaluate/blob/main/README.md) for more details on the code.

(Last update May 2026)

### [Accessibility Lens](https://accessibility-lens.onrender.com/)

Paste any public URL and see it through four sets of eyes: low vision, color blindness, keyboard-only navigation, and screen reader. The app fetches the raw HTML, runs 11 WCAG 2.1 rules (missing alt text, broken heading structure, low color contrast, zoom disabled, duplicate IDs, unlabelled form controls, and more), and gives a concrete fix for each failure. The signature feature is a screen-reader view that strips all layout and shows the page as the linear stream of roles and text a blind user actually hears — making failures visceral rather than abstract. With an Anthropic API key, Claude rewrites each offending snippet into a corrected one; without it, rule-based fixes still cover every issue. Built as a TypeScript monorepo (React + Vite client, Express server), deployed on Render. 102 tests passing, ~96% server coverage. Built from the `daily-project-ideas` prompt for 2026-05-12.

See [README](https://github.com/pisanuw/Claude-capstone/blob/main/accessibility-lens/README.md) for more details on the code or use it at <https://accessibility-lens.onrender.com/>

(Last update May 2026)

### [HTML Editor](https://github.com/pisanuw/html-editor)

A lightweight native macOS HTML editor built with SwiftUI, AppKit, and WebKit. Features a split-pane layout with a syntax-highlighted editor on the left and a live `WKWebView` preview on the right that updates automatically as you type. Includes a toolbar with one-click insertion of common tags (headings, bold, italic, links, lists), full file operations (New, Open, Save, Save As), and a status bar showing file path and cursor position. No web deployment — build and run from Xcode.

See [README](https://github.com/pisanuw/html-editor/blob/main/README.md) for more details on the code.

(Last update May 2026)

### [Digital Yusuf](https://chatwithdigitalme.netlify.app/)

A web app that lets you chat with a digital version of Yusuf Pisan. Built on a knowledge base of 10 structured persona files (~155K characters) covering bio, teaching philosophy, research, communication style, opinions, quirks, and full Substack articles — assembled from 30+ public sources including faculty pages, teaching evaluations, 63+ GitHub repos, Google Scholar, and promotion documents. The entire persona is loaded into the system prompt (no RAG needed at this scale). The digital Yusuf speaks in first person, matching his voice, humor, and opinions. Features streaming responses via SSE, optional Google Sign-In, BYOK (users can supply their own Anthropic API key), an admin dashboard with usage analytics and cost controls, and auto-email of finished conversations. Frontend is React + Vite on Netlify; backend is FastAPI on Render (Docker).

Chat with it at <https://chatwithdigitalme.netlify.app/>

(Last update May 2026)

### [Daily Project Ideas](https://github.com/pisanuw/daily-project-ideas)

Every morning at 5am, a Claude Code Remote Trigger wakes up, reads five subreddits (r/SideProject, r/sideprojects, r/ProductHunters, r/coolgithubprojects, r/AI_Agents), surfs the web, and commits three new project ideas to a public GitHub repo — prioritizing side projects, teaching tools, classroom assignments, and anything useful for students. By the time I sit down with coffee there is a fresh `YYYY-MM-DD.md` waiting. The repo also stores the full briefing, AI log, and change history so the prompt is version-controlled alongside the output. Read the Substack article [My Cron Job Reads Reddit. The Prompts Are in Git.](https://education2ai.substack.com/p/my-cron-job-reads-reddit-the-prompts) for the thinking behind it.

See [README](https://github.com/pisanuw/daily-project-ideas/blob/main/README.md) for more details on the code or browse the ideas at <https://github.com/pisanuw/daily-project-ideas>

(Last update May 2026)

### [Playful Interactions with AI](https://docs.google.com/presentation/d/e/2PACX-1vR5w8OC78eblbD9sOh3fNz5iK1Zgug63C4458P1lWfRAo_iolN09cCmLTA1Jgvn0WUy-QSmoivTUZmZ/pub?start=false&loop=false&delayms=5000&slide=id.p1)

An opening keynote on how faculty can keep themselves up to date with AI tools and support their students. Covers hands-on examples of using LLMs for teaching, grading, and course content — with a warm, collegial tone aimed at fellow academics. Available in [English](https://docs.google.com/presentation/d/e/2PACX-1vR5w8OC78eblbD9sOh3fNz5iK1Zgug63C4458P1lWfRAo_iolN09cCmLTA1Jgvn0WUy-QSmoivTUZmZ/pub?start=false&loop=false&delayms=5000&slide=id.p1) and [Turkish](https://docs.google.com/presentation/d/e/2PACX-1vQIyaIT3pzrBcvJ0ftY0pKvW5icMDLeuiM21FiVnF-faLxm-Z5w43kvRCdOFm8sfYY8hPu8nnRgSAUi/pub?start=false&loop=false&delayms=3000).

(May 2026)

### [Letter Game](https://letter-category.netlify.app/)

A casual browser word game where you and the computer alternate naming things in a chosen category, one letter at a time from A to Z. Choose from 20 categories (Animals, World Cities, Movies, Mythological Deities, Dinosaurs, and more) or let the game pick at random. You type a word, it's validated against the built-in word list, and the computer picks its own entry (with a Wikipedia image). You get 3 skips per game for tough letters. Built as a pure static site — plain HTML, CSS, and JavaScript with no framework or backend — using the Wikipedia REST API for images and Netlify Forms for word suggestions.

See [README](https://github.com/pisanuw/lettergame/blob/main/README.md) for more details on the code or use it at <https://letter-category.netlify.app/>

(Last update May 2026)

### [PasteMD](https://paste-md.netlify.app/)

A Markdown publishing tool with passwordless authentication. Users sign in via magic link (email), write or paste Markdown, and publish it as a rendered page with a short shareable URL. Posts are stored in Netlify Blobs (no external database required). Authors can manage and delete their own posts from a personal dashboard; admins get a separate panel to view and delete any post across all users. Admins are notified by email whenever a new post is published. Built as a pure static frontend with Netlify serverless functions handling auth (JWT-based), post CRUD, and email delivery.

See [README](https://github.com/pisanuw/pastemd/blob/main/README.md) for more details on the code or use it at <https://paste-md.netlify.app/>

(Last update April 2026)

### [Grade Histogram Plotter](https://grade-histogram-plotter.onrender.com/)

A lightweight Flask web app for visualizing grade distributions. Paste scores one per line (or upload a file), optionally customize the grade-bucket cutoffs, and get an instant histogram with summary statistics — mean, median, standard deviation, min, max, and per-bucket counts and percentages. Non-numeric entries are tallied in a separate NaN bucket. Includes CSRF protection and rate limiting. Deployed on Render.

See [README](https://github.com/pisanuw/grade-histogram-plotter/blob/main/README.md) for more details on the code or use it at <https://grade-histogram-plotter.onrender.com/>

(Last update April 2026)

### [UpvoteMe](https://upvoteme.netlify.app/)

A private, unlisted comment-and-voting app. Anyone can create a topic and instantly get two short URLs — one to share with participants, one private admin URL for moderation. Participants post comments (with optional file attachments, up to 5 files × 2 MB each) and upvote or downvote others. No public topic listing exists by design; topics are only reachable via shared URLs. Admins can lock or delete topics. Voting can be restricted to authenticated users (Google OAuth or magic link), in which case the admin can see who voted on each comment. Topics auto-delete after 30 days of inactivity.

See [README](https://github.com/pisanuw/upvote/blob/main/README.md) for more details on the code or use it at <https://upvoteme.netlify.app/>

(Last update April 2026)

### [RankMe](https://rankme-1ttb.onrender.com/)

A head-to-head voting app that ranks anything using the ELO rating system. Anyone can create a topic (movies, foods, photos, etc.), add items with optional images, and vote by repeatedly choosing between two randomly matched items. Rankings update in real time after each vote using a variable K-factor ELO algorithm (K=40 for new items, tapering to K=10 for established ones). Sessions are tracked via cookies to prevent repeat matchups in the same browser session. An admin panel at a secret URL allows deletion of topics and items.

See [README](https://github.com/pisanuw/rankme/blob/main/README.md) for more details on the code or use it at <https://rankme-1ttb.onrender.com/>

(Last update April 2026)

### [The AI Grading Paradox](https://docs.google.com/document/d/1NeDP4ELrnfuB2tjqXvEow_BTOVvblJLPH0gmuBuYstQ/edit?usp=drivesdk)

A classroom exercise for CSS 382 Introduction to Artificial Intelligence on how professors should grade homework in an era where AI can complete almost any assignment with near-perfect results. Groups of 5–6 students stress-tested four grading models (VIVA oral defense, GitHub audit, AI-hybrid rubric, and mastery/pass-fail), then designed their own "Ideal Grading Policy." The assignment and a synthesis report of student submissions (created with Gemini) can be found [here](https://docs.google.com/document/d/1NeDP4ELrnfuB2tjqXvEow_BTOVvblJLPH0gmuBuYstQ/edit?usp=drivesdk).

(Completed in April 2026)

### [The AI Learner's Dilemma](https://docs.google.com/document/d/1lJfZw5Zx3tpTuj8mr0k8rhk0bq9OSQmgh9o89tVJy8U/mobilebasic)

A classroom exercise for CSS 382 Introduction to Artificial Intelligence on the ethical dilemma students face when using AI for homework: prioritize learning and risk a lower grade, or prioritize grades and miss the learning opportunity. Groups of 5–6 students analyzed three personas (The Accelerator, The Proxy, The Traditionalist), assessed long-term consequences through the lenses of technical interviews, employer expectations, and academic integrity, then drafted a 5-rule "Personal AI Ethics Protocol." Near-unanimous consensus: The Accelerator is most sustainable, The Proxy is unethical, and a CS degree's value shifts from code-writing to engineering judgment in a world of capable AI. The assignment and a synthesis report of student submissions (created with Gemini) can be found [here](https://docs.google.com/document/d/1lJfZw5Zx3tpTuj8mr0k8rhk0bq9OSQmgh9o89tVJy8U/mobilebasic).

(Completed in April 2026)

### [Ranked Voting](https://ranked-voting.netlify.app/login)

A full-stack ranked-choice voting web app. Admins create contests with multiple candidates, set a number of winners, control voter access via allowed email lists, and optionally randomize option order per voter. Voters submit drag-and-drop ballots. Results are computed using step-by-step Instant Runoff Voting (IRV), showing each elimination round until winner(s) are determined. Built with React + Vite, Tailwind CSS, Supabase (PostgreSQL + Auth), and Netlify serverless functions.

See [README](https://github.com/pisanuw/ranked-voting/blob/main/README.md) for more details on the code or use it at <https://ranked-voting.netlify.app/login>

(Last update April 2026)

### [40 Greatest Innovations – Ordering Game](https://order-cards.netlify.app/)

A web-based card-ordering game where players arrange the 40 greatest innovations of all time in chronological order. Players drag or click cards across a deck, board, and "later" holding area, then press **Check Answers** to receive a final score (no hints during play). Supports drag-and-drop and touch.

See [README](https://github.com/pisanuw/Greatest-innovations/blob/main/README.md) for more details on the code or use it at <https://order-cards.netlify.app/>

(Last update April 2026)

### [ClaudeBot](https://discord.com/oauth2/authorize?client_id=1493464177875091596)

Allows users to ask Claude questions, get Claude to review code, suggest patches via Discord. Users need to use their own Anthropic API key (so I do not have to pay for my students' explorations!)

See [README](https://github.com/pisanuw/claude-discordbot/blob/main/README.md) for more details. You can install it on your own Discord server using [this link](https://discord.com/oauth2/authorize?client_id=1493464177875091596)

(Last update April 2026)

### [MeetMe](https://meetme.pisan.me/) — Joint Meeting Finder

Allows gathering information from multiple people on their availability, so you can find a common meeting time. You can also set it up to let users "book" you based on your availability. Combination of <https://www.when2meet.com/> <https://calendly.com/> and <https://doodle.com/>

See [README](https://github.com/pisanuw/meetme/blob/main/README.md) for more details on the code or use it at <https://meetme.pisan.me/>

(Last update April 2026)

### [Canvas Accessibility Fixer](https://canvas-accessibility.onrender.com/login)

Improves the accessibility score for Canvas pages automatically. Needs a canvas token to access Canvas pages.

See [README](https://github.com/pisanuw/canvas-accessibility/blob/main/README.md) for more details on the code or use it at <https://canvas-accessibility.onrender.com/>

(Last update April 2026)

### [TPS - Thermodynamics Problem Solver](https://tps-thesis-recreation.onrender.com/)

Based on my PhD thesis, starting to recreate the project from scratch.

Use it at <https://tps-thesis-recreation.onrender.com/>

To be completed at a later date!

(Last update April 2026)

### [Grade Statistics](https://github.com/pisanuw/gradeplotter/blob/main/README.md)

An internal project to generate graphs based on grades for each professor, for each course as well as historical data.

See [README](https://github.com/pisanuw/gradeplotter/blob/main/README.md) for more details on the code. Only used locally, so no web deployment.

(Last update April 2026)

### [Bullet Impact Simulator](https://targetbullet.netlify.app/)

A toy project on whether sensors could be used to determine where a bullet has hit on the target.

See [README](https://github.com/pisanuw/bullet/blob/main/README.md) for more details on the code or use it at <https://targetbullet.netlify.app/>

(Last update April 2026)

### [Cloud Games Portal](https://tic-tac-toe-app-857412880660.us-west1.run.app/)

Started with a simple version of Tic-Tac-Toe and ended up adding backgammon and chess as well. Nothing fancy, but was good for learning.

See [README](https://github.com/pisanuw/tictactoe/blob/main/README.md) for more details on the code or use it at <https://tic-tac-toe-app-857412880660.us-west1.run.app/>

(Last update April 2026)

### [Choose Your Own Adventure](https://github.com/pisan382/choose-your-own-adventure/blob/main/README.md)

Starter code for student projects. Students extended this project to create Choose Your Own Adventure authoring tools as well as Choose Your Own Adventure reading platforms.

See [README](https://github.com/pisan382/choose-your-own-adventure/blob/main/README.md) for more details on the code.

(Last update April 2026)

### [StockReptile](https://stockreptile.netlify.app/) - A Chess Playing Web App and Learning Tool

StockFish is the best chess engine out there. StockReptile is my inferior version but much more suited as a learning tool

See [README](https://github.com/pisanuw/notstockfish/blob/main/README.md) for more details on the code or use it at <https://stockreptile.netlify.app/>

(Last update April 2026)

### [Teaching Evaluation Graph Generator](https://pisanorg.github.io/yusuf/graphs/)

This tool automates the extraction of teaching evaluation metrics from historical course evaluation PDFs and visualizes them over time using line graphs.

See [README](https://github.com/pisanorg/yusuf/blob/master/code/README.md) for more details on the code or see my teaching evaluation dashboard at <https://pisanorg.github.io/yusuf/graphs/>

(Last update April 2026)

### [UW Course & Professor Finder](https://uwcourses.netlify.app/)

A web app from UW time schedule data so users can quickly answer:

* Which professor taught a specific course?
* Which courses did a specific professor teach?
* When (quarter and year) was the course offered?

The app supports all three UW campuses — Bothell, Tacoma, and Seattle — with a drill-down UI: select campus → select department → filter by course, professor, quarter, year.

See [README](https://github.com/pisanuw/01shortAIproject/blob/main/README.md) for more details on the code or use it at <https://uwcourses.netlify.app/>

(Last update April 2026)

### [The Algorithmic Professor? AI Ethics in the Classroom](https://docs.google.com/document/d/18IZ7V11PKwUP_kISJSU_7FRxD3sl8xbM8YOyZXdDB20/edit?tab=t.0)

A classroom exercise on what students think of the professors' use of AI in their teaching from generating slides to grading assignments with AI.

The assignment description and the summary report can be found [here](https://docs.google.com/document/d/18IZ7V11PKwUP_kISJSU_7FRxD3sl8xbM8YOyZXdDB20/edit?tab=t.0).

(Completed in April 2026)

### [CS Prof vs Gemini Prompts](https://docs.google.com/document/d/13HNdkUNjgwac0Uwg4OpIAtMr449614Y_x_z3ufXBTzc/edit?tab=t.0)

Previously I had used Gemini to create slides. This time it claimed it cannot create slides. This is a summary of my "discussion" with Gemini trying to understand why it is refusing and trying to figure out a better prompt to get it to do what it had done before. You can read my "discussion" [here](https://docs.google.com/document/d/13HNdkUNjgwac0Uwg4OpIAtMr449614Y_x_z3ufXBTzc/edit?tab=t.0)

(Completed in March 2026)

### [History of AI slides by Gemini Pro](https://drive.google.com/drive/u/3/folders/1prcrEZ3l9a3mb6PLQlIgOamQffSaJZ32)

I asked (guided?) Gemini Pro to create a set of slides on the History of Artificial Intelligence that I plan to use in my CSS 382 Introduction to Artificial Intelligence course in Spring at University of Washington Bothell.

I provided [History of Artificial Intelligence](https://en.wikipedia.org/wiki/History_of_artificial_intelligence) page from Wikipedia as a source. The slides produced by Gemini are [here](https://drive.google.com/drive/u/3/folders/1prcrEZ3l9a3mb6PLQlIgOamQffSaJZ32). I think it did a good job.

(Completed in March 2026)

---

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/stem/about/divisions/css) | [University of Washington Bothell](https://www.uwb.edu/)
