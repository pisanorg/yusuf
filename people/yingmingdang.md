# Photorealistic and Toon Shading

## Yingming Dang

The rapid advancement of computing hardware, especially Graphics Processing Unit (GPU), has allowed the rendering of increasingly complex images in real-time. Meanwhile, in the area of photorealism, the evolving illumination models are also becoming more capable of producing physically plausible images. In addition to photorealism, there’s also an increasing need for non-photorealistic rendering, which synthesizes images with specific artistic style or enhancements for applications such as technical illustration. Toon shading is one of the popular non-photorealistic rendering techniques that mimic the artistic style of traditional cartoons.

The goals of this project are to analyze, understand, and implement the illumination models typically found in modern commercial 3D graphical applications along with prominent toon shading techniques: color ramp and outline. We studied the evolution of photorealistic illumination approximations and then, based on the simple Lambertian model for diffuse reflection, we implemented recent variances and improvements of the Cook-Torrance microfacet based Bi-Direction Reflection Distribution Function (BRDF) specular reflection of light. We further improve our model by integrating the ground-truth ambient occlusion (GTAO) to better approximate ambient light inter-reflections. This physically-based photorealistic illumination model is then enhanced to support non-photorealism with color ramp and outline toon shader techniques.

The final illumination model is demonstrated with both simple geometric objects for highlighting specific effects and interesting and complex 3D models for verifying the general correctness. Our delivered illumination system supports a variety of parameters for users to fine-tune the desirable effects. The source code from this project, along with this documentation, serve as excellent references for those who are interested in understanding modern illumination models for real-time rendering and toon shading.

***

[Yusuf Pisan](https://pisanorg.github.io/yusuf/) | [Computing & Software Systems (CSS)](https://www.uwb.edu/css) | [University of Washington Bothell](https://www.uwb.edu/)
