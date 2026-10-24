# Put Your Course on DSA

The published deck for a talk for instructors: adding a course as a partnership, with CSS 430 Operating Systems as the worked example, and a section on what self-serve onboarding would take. 28 slides, about 30 minutes. Landing page: `index.md`, served at `pisanorg.github.io/yusuf/talks/202610DSA-YourCourse/`.

## Files

| File | What it is |
|------|-----------|
| `slides.html` | The deck, and its source: edit it here. It carries **no speaker notes**; they are kept outside the deck, in the private `dsa-instructor` repo under `research/202610DSA-YourCourse/NOTES.md`, keyed by slide number and title. |
| `slides.pdf` | Slides only. Regenerate it after any edit (below). |
| `img/` | Screenshots of DSA from a local copy with a throwaway SQLite database and made-up students. No production data. |
| `index.md` | The landing page: abstract, outline, links. |
| `vendor/reveal/` | Reveal.js 5.1.0 (core, white theme, notes plugin), vendored so the folder works with no network. |

Images:

- `chat-full.png`, `instructor.png`: a demo student and a demo class.

## Running it

Double-click `slides.html`, or serve the folder (`python3 -m http.server 8092`, then `http://localhost:8092/slides.html`). Keys: arrows or space to advance, `S` speaker window (timer and next slide), `F` full screen, `O` overview, `B` blank, `?` help.

## Regenerating `slides.pdf`

Any Chromium-based printer works. With decktape and Ghostscript, as for the Northwestern deck:

```bash
cd talks/202610DSA-YourCourse && python3 -m http.server 8731 &
decktape reveal http://localhost:8731/slides.html /tmp/raw.pdf --size 1280x720
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=slides.pdf /tmp/raw.pdf
```

Or with Playwright: open `slides.html?print-pdf` and call `page.pdf({preferCSSPageSize: true, printBackground: true})`. That is how the published copy was made.

## Before you present

- CSS 430's status (slide 16) is as of 24 October 2026. Update it before presenting.
- Step times are the runbook's estimates and 430's recorded runs, not guarantees.
- The voice slide (19) describes the code today: one persona for every course.
