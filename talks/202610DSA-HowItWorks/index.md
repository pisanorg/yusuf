---
layout: default
title: How DSA Works
page_class: page-talks
---

<div class="talk-meta">
  <span><strong>Technical talk</strong>, for CS faculty and engineers</span>
  <span>October 2026</span>
  <span>40 slides, about 45 minutes</span>
</div>

<div class="talk-actions">
  <a class="btn btn-gold" href="slides.html">Present the slides</a>
  <a class="btn btn-outline" href="slides.pdf">Download PDF</a>
</div>

<div class="bio-text">
DSA is the tutor I built for our data structures courses. Its job is to help students without handing them the answer, and a capable model asked to tutor hands over the answer by default. So the whole design comes down to one decision: the model writes the reply, and ordinary code decides what the reply may contain.
</div>
<div class="bio-text">
This talk is the system end to end. The offline pipeline that turns a course's slides, recordings and textbook into eight searchable collections, decks and practice banks. The ten stages every student message goes through, and who sees what at each one. The learner model that decides how much help a topic gets. And what it takes for one person to run it: deploys, spend caps, data rights, backups, and the tests that keep a lot of AI-written code from eroding the architecture. Mostly small, boring defences, each with a test.
</div>

## What is in it

<ol class="talk-outline">
  <li><strong>Building a course.</strong> Sources in, eight course-stamped collections out, two walls that keep answer keys away from students, and generated content that has to prove itself.</li>
  <li><strong>The supervised turn.</strong> Ten stages, an information-flow table, the hint ceiling as policy-as-data, the detector in the stream, the judge, and where it fails closed.</li>
  <li><strong>The learner model.</strong> One grade scale, a window of six, a forgetting curve, and how evidence sets the ceiling.</li>
  <li><strong>Running it.</strong> Manual deploys and a boot that never stops on an external, three payers and one function that decides, security, data rights, backups that have been restored.</li>
  <li><strong>Keeping it correct.</strong> Tests that read the code, simulated students at $0, a stronger model auditing the cheap one every night, and how the thing was built with Claude Code.</li>
  <li><strong>Lessons and open problems.</strong> Six things I would keep, and four I have not solved.</li>
</ol>

<div class="summary-block">
No student data is in this deck. The numbers are content and code counts from the repository, development-time estimates (labelled as such), and one local demo run with a made-up student and every model call through the <code>claude</code> CLI.
</div>

## Presenting it yourself

The slides are plain HTML with Reveal.js sitting next to them, so the folder works with no network. Arrow keys or space to advance, <code>S</code> for the speaker window (a timer and the next slide; these decks carry no notes), <code>F</code> for full screen, <code>O</code> for the slide overview, <code>B</code> to blank the screen, <code>?</code> for help. Feel free to borrow any of it.

<div class="summary-links">
  <a href="../">All talks</a>
  <a href="../202610DSA-ForFaculty/">The pedagogy talk</a>
  <a href="https://github.com/pisanorg/yusuf/tree/master/talks/202610DSA-HowItWorks">Source on GitHub</a>
  <a href="https://digital-student-assistant.com">DSA, the tutor itself</a>
</div>
