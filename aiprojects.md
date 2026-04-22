# Adventures in AI

I got my PhD in 1998 from Northwestern University. My PhD was in AI, specifically in qualitative reasoning, diagrammatic reasoning and problem solving. My PhD was in what would be considered in GOFAI (Good Old Fashioned AI). It relied on hand built models and ontologies. It used a truth-maintenance system and with hand-built pattern-matching rules to maintain its knowledge base. The system I built could solve 150 problems from a university level thermodynamics textbook. It was a big achievement for its time.

Today's AI is much different. Lots of statistical models, lots of data, automated systems that take millions of dollars to train and have billions of parameters.

LLMs are going to change the world as we know it. AI systems can already implement software projects that used to take teams weeks to complete. They can already hold conversations, provide advice, assist in brainstorming and make suggestions.

I started playing with these new systems (Claude, Gemini, ChatGPT, Microsoft CoPilot, GitHub CoPilot, etc) in March 2026. Below are some of the projects I have built in reverse chronological order.

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

See [README](https://github.com/pisanuw/tps/blob/main/README.md) for more details on the code or use it at <https://tps-thesis-recreation.onrender.com/>

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

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
