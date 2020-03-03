# Real time Ray tracing in Unity

## Kaihua Hu

Ray tracing is an important rendering algorithm that naturally supports advanced effects such as realistic reflections, refractions, and shadows. It is capable of synthesizing images with striking realism that are comparable to photographs or videos captured in the real world. However, due to the intensive computation requirements and limitations of traditional hardware, ray trace image generation has largely been limited to off-line batch processing. Recently, with the increasing performance of the hardware, the latest Graphics Processing Units (GPUs) are becoming capable of delivering the computation requirements of ray tracing in real-time.

In this project, we implemented a real-time ray tracing system based on the Unity game engine platform. Our system delivers typical rendering features via a ray-tracing pipeline, where the features include camera manipulations, anti-aliasing, environmental mapping, and supports for customized mesh models, materials, light sources, Phong illumination, reflection, and shadow. Additionally, our system also provides simple User Interfaces (UI) for Unity users to configure the rendering process in real-time. For example, the user can define a skybox and increase the number of samples for anti-aliasing. They can even modify the material properties and generations of reflection rays, all in real-time, while the ray trace rendering system is running.

We have carefully examined the performance of our real-time ray tracing system and identified bottlenecks. Somewhat surprisingly, the performance results indicated that the communication between the CPU and GPU was not a limiting factor. Instead, as expected in all ray tracing systems, the number of ray intersection computation was the main issue. In our case, the vast proportion of frame time was spent in the GPU computing intersections. This bottleneck was relieved with an acceleration KD-Tree spatial structure. With the acceleration structure, the bottleneck of the system switched to the KD-Tree construction computation in the CPU. We addressed this issue by applying a lazy updating strategy for the KD-Tree construction. With these optimizations, based on our benchmark scenes, the resulting system was able to achieve over 100-times speed up, from rendering 144 triangles to 17000 triangles in real-time.

***

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
