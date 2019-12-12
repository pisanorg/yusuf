# Project Tablet-based Remote Control of Ultrasound Device

## Nathan Phan

During the summer, I interned at Siemens Healthineers as a technical intern. Siemens Healthineers is a company
with a location in Issaquah that focuses on the development of ultrasound devices for the healthcare field.
The main task that I worked on over the summer for my capstone project was to design and develop a working
proof of concept application to facilitate the control of ultrasound software on a separate device over a network.

There were multiple iterations of the project that changed as different requirements and use-cases came.
Originally, the project was only intended to be a C# program that made use of a VNC variant’s API to allow the
remote control of an ultrasound machine over the same local network. However, the project eventually involved
the development of C#, WPF, and XAML code on the pre-existing codebase with the Google RPC library (gRPC)
to facilitate communication. The first version to use gRPC involved the definition of relevant methods for the
ultrasound software using protocol buffers a type of file used by gRPC to define messages for serialization
and communication. The second iteration of the project involved streamlining the development process by using
reflection and the proxy pattern to intercept the types and messages sent from the remote platform rather than
implementing every combination of functions and message types.

This project involved performing several duties of a software engineer, including the development of diagrams,
the documentation of the project, participating in standups and formal meetings with the stakeholders and
providing concise and informative updates. I found myself using the Microsoft development stack of MSTest for
testing, Visual Studio for an IDE, Team Foundation Server as version control, Gliffy for diagramming, and
Confluence for documentation.

At the end of the internship, I was able to deliver a responsive application that supported much of the ultrasound
functionality. The final iteration was built using C#, WPF, XAML, and Google RPC (gRPC), successfully built,
tested, and deployed on a Windows Surface. The results were satisfactory, and the code base exists as a
separate branch.

***

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
