# A Deep Dive into Manim's Internals

> Source: https://docs.manim.community/en/stable/guides/deep_dive.html

## Overview

This comprehensive guide by Benjamin Hackl explains Manim's rendering process, focusing on the Cairo renderer as of version v0.16.0. The documentation covers three main phases: preliminaries (setup before rendering), mobject initialization, and animations with the render loop.

## Preliminaries

The guide explains that importing Manim via `from manim import *` initializes the global configuration system. The rendering process always involves instantiating a Scene object and calling its `render()` method, whether through the CLI, Jupyter notebooks, or direct Python scripts.

"The Scene then asks its renderer to initialize the scene by calling `self.renderer.init_scene(self)`" which sets up the `SceneFileWriter` for handling video output through FFMPEG.

## Mobject Architecture

The documentation identifies three renderable mobject types for Cairo:

| Type | Description |
|------|-------------|
| `ImageMobject` | For displaying images |
| `PMobject` | For point clouds |
| `VMobject` | Vectorized mobjects using Bézier curves |

"VMobjects represent vectorized mobjects...the camera looks at the `points` attribute of a VMobject and divides it into sets of four points each."

Each set of four points forms a cubic Bézier curve with anchors (endpoints) and handles (control points).

## Scene Management

"Scene.add() adds the mobject to the list of mobjects that should be rendered...in a very careful way to avoid the situation that a mobject is being added to the scene more than once."

The `Scene.restructure_mobjects()` method prevents duplicate rendering by flattening nested structures when mobjects already exist in the scene.

## Toy Example

The guide uses a concrete example creating a Square, transforming it to a Circle, adding a Dot with an updater, and performing animations — demonstrating how initialization chains work through inheritance hierarchies.

## Further Reading

The ongoing developer wiki lives at: https://github.com/ManimCommunity/manim/wiki/Developer-documentation-%28WIP%29
