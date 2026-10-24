# Meet DSA, Your Course Tutor

The published deck for a ten-minute, course-neutral orientation for students in week 1. 14 slides, about 10 minutes. Landing page: `index.md`, served at `pisanorg.github.io/yusuf/talks/202610DSA-ForStudents/`.

## Files

| File | What it is |
|------|-----------|
| `slides.html` | The deck, and its source: edit it here. It carries **no speaker notes**; they are kept outside the deck, in the private `dsa-instructor` repo under `research/202610DSA-ForStudents/NOTES.md`, keyed by slide number and title. |
| `slides.pdf` | Slides only. Regenerate it after any edit (below). |
| `img/` | Screenshots of DSA from a local copy with a throwaway SQLite database and made-up students. No production data. |
| `index.md` | The landing page: abstract, outline, links. |
| `vendor/reveal/` | Reveal.js 5.1.0 (core, white theme, notes plugin), vendored so the folder works with no network. |

Images:

- `welcome.png`, `chat-full.png`, `chat-refusal.png`, `chat-attempt.png`, `readiness.png`, `character.png`: a demo student's pages; the tutor's replies are real supervised replies from a local run.

## Running it

Double-click `slides.html`, or serve the folder (`python3 -m http.server 8092`, then `http://localhost:8092/slides.html`). Keys: arrows or space to advance, `S` speaker window (timer and next slide), `F` full screen, `O` overview, `B` blank, `?` help.

## Regenerating `slides.pdf`

Any Chromium-based printer works. With decktape and Ghostscript, as for the Northwestern deck:

```bash
cd talks/202610DSA-ForStudents && python3 -m http.server 8731 &
decktape reveal http://localhost:8731/slides.html /tmp/raw.pdf --size 1280x720
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=slides.pdf /tmp/raw.pdf
```

Or with Playwright: open `slides.html?print-pdf` and call `page.pdf({preferCSSPageSize: true, printBackground: true})`. That is how the published copy was made.

## Before you present

- The limits slide says "a daily limit" rather than a number, since the value is configuration and changes.
- If a feature switch is turned off in production, its line on the Help page disappears; keep the deck in step with the live Help page.
