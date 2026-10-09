# 75-minute talk: Teaching an LLM Tutor to Withhold the Answer

One talk assembled from the two standalone ones:

- the literature review, `socratic-tutoring-talk` (42 slides, 60 min), and
- the SIGCSE 2027 system talk, `sigcse2027/talk` (38 slides, 60 min).

Both source decks live in the private research repo, not here.

**Audience:** a general CS faculty colloquium — mixed systems, theory and AI;
interested in whether to use this in their own courses, not specialists in
learning science or in LLM internals.
**Shape:** about 68 minutes of talk (an eleven-minute opening, then a 5-minute
live demo) + what is left of the 75 for discussion. 64 slides.
**Spine:** evidence first, then the system. Parts 1–4 are the literature; the
hinge is slide 35; parts 5–8 are one attempt to build what the literature asks
for, and what broke.

The two source decks are untouched and still presentable on their own. This deck
carries its own copy of Reveal, so all three folders are independent.

## Files

| File | What it is |
|------|-----------|
| `slides.html` | The deck. 64 slides (8 section dividers), speaker notes in `<aside class="notes">` on every slide. |
| `img/` | The photographs and screenshots used by the opening slides (the Rock, the contribution graph, the digital twin, the banned session, and the five screens of YPDSA itself). |
| `SCRIPT.md` | Timing spine, cut order, 45- and 30-minute versions, the demo runbook, numbers to say out loud, prepared answers. Gitignored: speaker-private. |
| `slides.pdf` | Slides only, no notes. Published; linked from the landing page. Regenerate with `decktape reveal http://localhost:8731/slides.html slides.pdf --size 1280x720` while serving the folder. |
| `combined-talk-presenter.pdf` | One page per slide: the slide above, its speaker notes below. Gitignored (14 MB, and the notes are not for publication) — regenerate with `python scripts/make_presenter_pdf.py` in the research repo, or `--scale 1` for a 5.9 MB copy. |
| `index.md` | The published landing page at `pisanorg.github.io/yusuf/talks/202610Northwestern`: abstract, outline, links to the deck and the PDF. |
| `vendor/reveal/` | Reveal.js 5.1.0 (core, white theme, notes plugin), vendored so the folder works with no network. |

## Running it

Double-clicking `slides.html` works for presenting. For the **speaker-notes
window** (`S`) Reveal needs http, so serve the folder:

```bash
cd talks/202610Northwestern && python3 -m http.server 8092
# then open http://localhost:8092/slides.html
```

Keys: `→`/`space` next, `S` speaker notes, `F` full screen, `O` slide overview,
`B` blank the screen, `?` help.

## What was kept, and what was cut

**From the literature talk (18 of 42 slides).** Kept: the definition and the
active ingredient, the effect-size band, the assistance dilemma, the four method
families, what industry ships, both failure modes, the whole "does it help"
section, the two computing-education slides, the design policy, and the open
problems.

Cut, with the reason:

| Cut | Why |
|-----|-----|
| Pre-LLM tutors, neural tutoring (SOC 10–11) | History this room will grant you; AutoTutor's ≈ 0.8 SD survives as one line on slide 17's notes. |
| Reward design / the RL frontier (SOC 15) | The deepest ML slide in either deck, and the one a general faculty audience needs least. One line of slide 21's notes carries "you cannot simply train it in." |
| "Not one study" and the head-to-heads (SOC 23, 25) | Supporting detail for a claim slides 27 and 29 already make. |
| Programming hints (SOC 30) | Overlaps the design policy on slide 34. |
| Benchmarks, judges and simulators (SOC 33–34) | The evaluation argument is made concretely in part 5 with your own instrument instead. |
| Form rules (SOC 37) | Six practical rules, none of which the second half needs. |
| "Close to home" (SOC 39) | Superseded: the second half *is* the speaker's own tutor, in more detail. |

**From the SIGCSE talk (18 of 38 slides).** Kept: the problem named, why a prompt
cannot carry it, the hint ladder, the trust boundary, the two checks, the gates,
the personas, the two disciplines, the entire over-help ladder (Run 1 through
Rung 4, the finding and the mechanism), the demo, and the study.

Cut, with the reason:

| Cut | Why |
|-----|-----|
| "What trusted state actually is" (SIG 12) | Reviewer-driven detail; the trust-boundary slide carries the argument for this room. |
| "This is coding, not benchmarking" (SIG 18) | Aimed at SIGCSE's qualitative-methods readers. |
| The gate numbers table (SIG 28) | You already say the percentages are not the finding; the slide invites the question you do not want. |
| Reviewer scores (SIG 33), and the four criticisms (SIG 34) | Inside-baseball for a venue this room did not submit to. The deck does not mention the review at all; the limits it needs are carried by the study slide and the takeaways. |
| Full reference list (SIG 38) | The reading list on slide 61 is the one to leave up (the full references follow on 62–63), and both repositories are named on it. |

**Written for this deck:** the title, the personal opening (slides 2–6: the
Rock, the contribution graph, the two digital-twin slides and the banned
session), the five-screen tour of YPDSA (slides 7–11), the two-sentence thesis
(slide 12), the roadmap, four of the eight dividers, the merged takeaways
(slide 59), the merged three questions (slide 60), two full-citation reference slides
(62–63) and the closing Questions slide (64).

## Before you present

1. **Fill in slide 55** (`Fallback — captured run`) with screenshots from a
   pre-talk demo run. The box on that slide lists which three captures to take.
   Do this even if you intend to demo live.
2. **Demo setup** — two windows: the chat on the left
   (`.venv/bin/uvicorn ypdsa.main:app`), `/admin` scrolled to the turn-events
   table on the right. A **throwaway database and a non-admin synthetic
   student**, never production data. The four demo prompts are in `SCRIPT.md` §4.
3. **Check the dates.** Several 2026 sources were preprints when the slides were
   written (October 2026). If you give this talk months later, check whether any
   has been published, and update the label on the slide.
4. **Run the numbers past `SCRIPT.md` §3** so what you say matches the slides.
5. **Rehearse the hinge** (slide 35). The honest version — "I built the system
   first and read the literature afterwards" — is the line that makes the two
   halves one talk.

## Things in the deck that are claims to handle with care

Carried from both source decks, and still true here:

- **Bastani et al. (slide 27) shows effect sizes.** The "−17%" is the paper's own
  figure; the SD conversions (≈ −0.19 and ≈ −0.01) come from the Contractor &
  Reyes re-analysis, and the slide says so.
- **VanLehn's 0.79 / 0.76 / 0.31** (slide 17) come from his slides and secondary
  summaries, not the full paper.
- **Kestin et al.'s 0.63 SD** is disputed by an independent re-analysis, and the
  study did not test answer withholding.
- **Wang & Fan (2025) was retracted in 2026** (slide 29), after 500+ citations.
- **"Claude Learning mode is a system prompt"** (slide 22) rests on press
  coverage; Anthropic has not published how it works.
- **The auditor is the actor-class model** (`claude-sonnet-4-6` in
  `ypdsa/agent/models.py` in the research repo) — the same family as the
  actor it grades. Slide 43 says so. Expect a self-preference question and
  do not overclaim independence.
- **The constructive-code floor is a pedagogical claim** ("showing your work
  should buy you help"), not a software correction.
- **The behavioural state-gaming hole** (feign low mastery, fail a check on
  purpose, paste broken code to trip the floor) is real and unmitigated. It is
  no longer on a slide of its own — SIG 12 was cut — so be ready to name it
  yourself rather than have it found from the floor.
- **Nothing in the second half is evidence that a student learned anything.** The
  evaluation is automated, about two dozen scripted turns, no human subjects and
  no student data. Slide 59 says so; keep saying it.
