# Capstone and Project Ideas

This document is located at <https://pisanorg.github.io/yusuf/capstone-ideas.html>

Below are some potential capstone and project ideas.
I am open to supervising a much broader range of capstone topics. I prefer students who have already
taken some of my courses, and have done well in them, but even if you did not shine in the classroom,
you can still pitch your project. See [past capstone projects](https://pisanorg.github.io/yusuf/people)

For Summer 2020 and 2021, I am especially looking for students for 1000 Problems with Automated Feedback, Games for Change, 100 Unity Mechanics for Programmers, and Building a Mind: Everyday Reasoning to Expert Reasoning.

## Computer Science Education

### 1000 Problems with Automated Feedback

The goal of this project is to build the tools and content to provide
automated feedback to students on a large set of programming
problems. This project will require multiple teams of students and
will likely go on for several years. Each capstone project will make a
specific contribution. There are several parts to the project:

1. Creating the problems and solutions in a structured way. For each problem, there might be 5-10 variations. The text for each problem, the solution, tags and possible hints has to be individually crafted. You will explore how to create a structure to ensure consistency across problems as well as writing the solution to problem. DocBook is a possible format, but will probably have to be expanded.

2. Compiling and presenting problems. The problems might be stored in a database or a set of directories. You will explore how they can be compiled and presented as an easy to navigate set of web pages.
Feedback tools. Checking that a program compiles and the input-output matches for a large set of tests is the first step, but we can do so much more in terms of providing feedback. For C++, clang-tidy <https://clang.llvm.org/extra/> has a large number of checks. Some of the checks also propose fixes. Building a similar system, or a set of systems, for Java is part of the goal.

3. Instructor imitator. Different instructors provide different feedback to students, or even the same instructor might provide different feedback on assignment-1 versus assignment-5. Capturing these preferences and customizing the feedback based on problem and instructor persona is the goal for this project.

4. Building on top of existing tools. The systems we build need to work with existing tools and formats, but we may need to build bridging applications. For example, GitHub Actions can be used to provide feedback, but we may want to provide another interface that interfaces with GitHub and other programs rather than asking the end user to learn and use multiple systems. Using YAML to express configuration information rather than building our own tools from scratch.

5. Knowledge tracker. Tracking user knowledge based on what programs they have completed, suggesting programs to enhance their knowledge or suggesting programs to ensure they have sufficiently grasped the concept.

6. Testing and Evaluation: Having this system integrated into a course would be ideal, but there is other testing and evaluation that can be done through talking to experts and surveying students. Looking at the existing literature on how to evaluate action research. Do we expect students to have higher course scores when using this system? Do we expect them to feel different? Do we expect them to be more self-directed learners? How would we measure each of these hypotheses?

### Misconceptions

- Novice programmers have lots of misconceptions on how the program works.
Until those misconceptions are identified and corrected, these students will continue to
struggle.

  - Create a large catalog of misconceptions. [[1](https://dl.acm.org/citation.cfm?id=1734299),
  [2](http://csteachingtips.org/),
  [3](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C48&q=cs1+student+misconceptions&btnG=)
  ]

  - Take 3-5 misconceptions and create diagnostic tools for identifying
  if a student has those misconceptyions or not. The diagnostic tool can be a web based survey,
  an interview or in some other format.
  - Create a set of web-based, self-guided exercises where
  students can examine their own misconceptions and correct them.
  
- Feedback is crucial to learning, but students often receive limited feedback. There are industrial strength tools that can be used to provide feedback, but these tools often produce cryptic messages which confuse novice programmers even more. There are many systems that test a given program on a large set of possible inputs to determine if the program is correct, such as [zybooks](https://www.zybooks.com/), [leetcode](https://leetcode.com), [codelab](https://www.turingscraft.com/), [recurtutor](https://vtechworks.lib.vt.edu/handle/10919/64249), [uAssign](https://www.ideals.illinois.edu/handle/2142/101068) etc. These systems are useful because they are easy to build, but do not incorporate any pedagogical knowledge. They have no way of guiding a student to a suitable next problem based on the types of mistakes (or misconceptions) observed. There is much that can be done in this area.

For novice students, using complex tools to analyze programs can be difficult and frustrating. Create a web-based system that can enforce and check the assignment constraints. For example, an instructor might want the assignment submitted as an `ass.zip` file with specific files in it whereas another instructor might request individual files to be uploaded. Creating a language (i.e. simple configuration file) that can be used by instructors and a front-end that can check students' will be useful.
  
### Non-Traditional CS Students

We need to attract and retain nontraditional CS students. There is work to be done at university, high school,
and middle school levels as well as societal perceptions. [Research](https://www.tandfonline.com/doi/abs/10.1080/0163853X.2015.1136507) shows that facts alone are not sufficient to change beliefs. Explore how we can change beliefs about CS at any of the levels.

### CS for Social Good

[CS for Social Good](http://www.sigcas.org/csged/). Projects that make the world a better place.

## Artificial Intelligence

AI is much more than machine learning. I am intyerested in symbolic artificial intelligence and explainable artificial intelligence.

### Building a Mind: Everyday Reasoning to Expert Reasoning

There are lots of way to get computer to process facts and reach conclusions: case-based reasoning, analogical reasoning, qualitative reasoning, theorem provers, rule engines, classifiers, machine learning systems, etc. Some of these reasoning systems also allow the programs to explain "how" they reached their conclusion and "why" the conclusion is valid.

For this project, we will use <http://pyke.sourceforge.net/> (or a similar program) to build a set of different reasoners from Building Problem Solvers <http://www.qrg.northwestern.edu/BPS/BPS-Searchable.pdf> Each chapter can be viewed as a separate project. For each chapter, a set of web pages with examples of solving a specific set of problems will be created.

A more ambitious goal and an extension of this project will be to use NextKB <http://www.qrg.northwestern.edu/nextkb/index.html> on a set of different reasoning tasks

## Video Games / Augmented and Virtual Reality

### Games for Change

<http://www.gamesforchange.org/> aims to drive real-world impact through games and immersive media. Pick a goal that you care about, gather some background information on the topic, find an angle to turn it into a game. 50% of this project is the research on the goal topic and 50% on implementation. Topics such as "climate change" or "recycling is important" are too broad to address in a single game. Have a look at some of Ian Bogost's games at <http://bogost.com/games/persuasive_games_1/>; understand why Airport Security game is a satire. Examine games from <http://blog.h1n1.influenza.bvsalud.org/en/2009/10/07/find-out-more-about-influenza-by-playing-games/> helps people understand influenza a bit better. Your idea needs to be sophisticated enough and you need to be able to express why the opposite sides/perspectives have their own valid structured reasons for their position. The final deliverable for this project will be a position document and a simple, tested working game.

### 100 Unity Mechanics for Programmers

Even for experienced programmers, Unity provides a challenge. There are lots of different ways of doing things and finding the correct tutorial and extracting the right Unity function can be very difficult especially for newcomers who are not familiar with vocabulary. This project will produce 100 sample programs where each program demonstrates a different mechanic.

For example, WASD for movement will be a Unity program that shows how an object would move using WASD keys. Nothing more. Jumper might be a program that shows how to execute a jump like action with different parameters. We can use <https://inventwithpython.com/blog/2012/07/30/need-a-game-idea-a-list-of-game-mechanics-and-a-random-mechanic-mixer/> for different mechanics as well as Physics for Game Developers <http://shop.oreilly.com/product/0636920012221.do> to implement each mechanic. Each mechanics will be demonstrated as simply as possibly and have a corresponding web page that explains it.

## Something Different

If you have an idea that does not fit into the above categories, you are still welcome to pitch it. Follow the advice from <https://csedresearch.org/conducting-research/> and include the following four headings in your proposal.

  1. Research question - what will be the new knowledge
  2. Approach - building a software, running surveys, examining literature
  3. Evaluation - how do we evaluate the end result, what would be classified as a successful result and what would be unsuccessful
  4. Existing Research - what has been done that is similar to this, what research does this project follow from. Must have at least 3 references

***

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
