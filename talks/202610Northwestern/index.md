---
layout: default
title: Teaching an LLM Tutor to Withhold the Answer
page_class: page-talks
---

<div class="talk-meta">
  <span><strong>Northwestern University</strong>, CS faculty colloquium</span>
  <span>October 2026</span>
  <span>64 slides, 75 minutes</span>
</div>

<div class="talk-actions">
  <a class="btn btn-gold" href="slides.html">Present the slides</a>
  <a class="btn btn-outline" href="slides.pdf">Download PDF</a>
</div>

<div class="bio-text">
I run a Claude-backed tutor for our data structures courses, and that tutor's main job is to not give students the answer. At some point I realised I had built a lot of machinery on an assumption I had never checked: that withholding the answer is good for learning. So I went and read everything I could find. That is the first half of this talk, and it is a literature review, not a results talk.
</div>
<div class="bio-text">
The second half is what happened when I tried to make a model actually do it, and measured whether it did. Three things I would keep: withholding protects but rarely accelerates, so budget about 0.2 SD rather than two sigma; the decision you care about belongs in ordinary code instead of a prompt, because prompt-only withholding leaks; and every rejection should state its reason, or a score never becomes a diagnosis. I built the system first and read the literature afterwards, which is the honest order rather than the tidy one.
</div>

## What is in it

<ol class="talk-outline">
  <li><strong>What "Socratic" means.</strong> A countable behaviour, an active ingredient, and the effect size you should actually expect.</li>
  <li><strong>How LLM tutors are built, and how they fail.</strong> Four method families, what the vendors ship, and failures at both ends of the assistance dilemma.</li>
  <li><strong>Does it help students learn?</strong> Guardrails prevent harm. Gains come from structure. And students skip the help they most need.</li>
  <li><strong>Computing education.</strong> The largest guardrailed deployments anywhere. All of them leak, and upper-level courses are barely studied.</li>
  <li><strong>Building one that actually withholds.</strong> An eight-rung hint ladder, a trust boundary outside the model, and how you measure a refusal.</li>
  <li><strong>The over-help ladder.</strong> What a capable model does when you tell it not to help, and keep checking.</li>
  <li><strong>Live demo.</strong> I try to extract a solution from my own tutor. Second screen shows the machinery.</li>
  <li><strong>What we still cannot say.</strong> The criticisms I cannot argue with, the open problems, and the study I do not know how to design alone.</li>
</ol>

<div class="summary-block">
The scope, stated plainly: the second half is an architecture and a calibration method, checked against safety gates on about two dozen scripted turns. No human subjects, no student data. It is not evidence that a single student learned a single thing.
</div>

## Presenting it yourself

The slides are plain HTML with Reveal.js sitting next to them, so the folder works with no network. Arrow keys or space to advance, <code>S</code> for the speaker notes window, <code>F</code> for full screen, <code>O</code> for the slide overview, <code>B</code> to blank the screen, <code>?</code> for help. Every slide carries its notes. Feel free to borrow any of it.

<div class="summary-links">
  <a href="../">All talks</a>
  <a href="https://github.com/pisanorg/yusuf/tree/master/talks/202610Northwestern">Source on GitHub</a>
  <a href="https://ypdsa.pisan.me">YPDSA, the tutor itself</a>
</div>
