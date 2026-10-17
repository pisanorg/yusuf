# Changes

Format: `YYYY-MM-DD [type] description` (max 200 chars). Types: decision, plan, doc, scope, code, note.

2026-05-09 [note] Initialized.
2026-08-27 [doc] aiprojects: repointed Game Palette Inspector README link from pisanuw/c1 to Claude-capstone/game-palette-inspector after the monorepo move. Live URL unchanged.
2026-08-27 [doc] aiprojects: repointed Pathfinding Playground README link from pisanuw/pathfinding-playground to Claude-capstone/pathfinding-playground after the monorepo move. Live URL unchanged.
2026-09-25 [doc] aiprojects: added CSS Scheduler (pisanuw/css-scheduler, uwb-css-scheduler.netlify.app) at the top.
2026-09-30 [doc] aiprojects: added Where Does It Say (Claude-capstone/where-does-it-say, where-does-it-say.netlify.app) at the top.
2026-10-11 [scope] 202610Northwestern: speaker notes removed from the published deck. The notes-bearing master, SCRIPT.md and CLAIMS-REVIEW.md moved to a private repo; slides.html is now generated from it.
2026-10-11 [scope] Deleted AI-log.md. It was world-readable here, logged instructions verbatim, and nothing requires it; left in history by choice. .githooks/pre-commit refuses a deck carrying speaker notes (install: git config core.hooksPath .githooks).
2026-10-11 [doc] 202610Northwestern: four detail slides added (39a-39c under the trust boundary, 42a the fourteen-persona sim); slide counts 64 -> 68; preprint labels re-checked, all four still preprints; DEMO-RUNBOOK.md records what changed since it was verified on 10-09.

2026-10-11 [doc] 202610Northwestern: slide 39 lists the eight pre-classifier intents; slides.pdf regenerated for the 68-slide deck (decktape needs --chrome-path here, and a Ghostscript pass to stay ~3 MB rather than 12 MB) and the two-step command is in the README.
2026-10-11 [doc] 202610Northwestern: slide 29 drops the paywalled caveat from the visible line; the eight pre-classifier labels move onto 39a beside the classifier example; new slide 42b lists the fourteen personas, one line each. 69 slides; slides.pdf regenerated.
2026-10-11 [doc] 202610Northwestern: new slide 39d (what the strategist is given and what it returns, with the real merge outcomes); 39a and 39c now state where the eight intents and twelve moves came from, with the Graesser 2005 and Atkinson, Renkl & Merrill 2003 citations (the latter added to REFERENCES.md); 42b split into six archetype headings. 70 slides; slides.pdf regenerated.

2026-10-16 [doc] aiprojects: table of contents added at the top, 69 entries newest-first, 3-column .project-toc in style.scss, with an HTML-comment note telling future agents to keep it in sync.
2026-10-16 [doc] YPDSA renamed Digital Student Assistant, now at digital-student-assistant.com (old ypdsa.pisan.me 302s there). Changed in aiprojects.md and index.md; talks/202610Northwestern left alone.
