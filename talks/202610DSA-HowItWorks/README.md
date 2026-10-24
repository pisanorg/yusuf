# How DSA Works

The published deck for a technical talk for CS faculty and engineers: the content pipeline, the supervised turn, the learner model, operations and quality engineering. 40 slides, about 45 minutes. Landing page: `index.md`, served at `pisanorg.github.io/yusuf/talks/202610DSA-HowItWorks/`.

## Files

| File | What it is |
|------|-----------|
| `slides.html` | The deck, and its source: edit it here. It carries **no speaker notes**; they are kept outside the deck, in the private `dsa-instructor` repo under `research/202610DSA-HowItWorks/NOTES.md`, keyed by slide number and title. |
| `slides.pdf` | Slides only. Regenerate it after any edit (below). |
| `img/` | Screenshots of DSA from a local copy with a throwaway SQLite database and made-up students. No production data. |
| `index.md` | The landing page: abstract, outline, links. |
| `vendor/reveal/` | Reveal.js 5.1.0 (core, white theme, notes plugin), vendored so the folder works with no network. |

Images:

- `chat-full.png`: real supervised replies, produced by running the app's `run_turn` with every model call answered by the `claude` CLI (the persona simulator's transport, `tests/sim/cli_transport.py` in the private repo), for a demo student, beside a stand-in deck rendered from the lecture plan.

## Running it

Double-click `slides.html`, or serve the folder (`python3 -m http.server 8092`, then `http://localhost:8092/slides.html`). Keys: arrows or space to advance, `S` speaker window (timer and next slide), `F` full screen, `O` overview, `B` blank, `?` help.

## Regenerating `slides.pdf`

Any Chromium-based printer works. With decktape and Ghostscript, as for the Northwestern deck:

```bash
cd talks/202610DSA-HowItWorks && python3 -m http.server 8731 &
decktape reveal http://localhost:8731/slides.html /tmp/raw.pdf --size 1280x720
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=slides.pdf /tmp/raw.pdf
```

Or with Playwright: open `slides.html?print-pdf` and call `page.pdf({preferCSSPageSize: true, printBackground: true})`. That is how the published copy was made.

## Before you present

- The ledger rows and the judge's verdict on slides 21 and 23 come from that same local run, not from production.
- Cost figures are development-time estimates from June 2026 or arithmetic on list prices; the slides say so.
- Test, code and content counts were read from the private repo on 24 October 2026 and drift as it changes.
