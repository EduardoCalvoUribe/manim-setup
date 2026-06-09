# Quickstart

> Source: https://docs.manim.community/en/stable/tutorials/quickstart.html

## Overview

Manim is "an animation engine for precise programmatic animations." This quickstart introduces you to creating animations through command-line scenes, animating shapes, positioning objects, and using the `.animate` syntax.

## Starting a New Project

Initialize a project with:

```bash
manim init project my-project --default
```

This creates a project folder containing necessary Manim files and output directories.

## Animating a Circle

Create `main.py` with a basic scene:

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
```

Render with:

```bash
manim -pql main.py CreateCircle
```

### Key Concepts

The `from manim import *` statement imports all library contents. Most animation code resides in the `construct()` method of a `Scene` subclass. The `Create` animation displays objects on screen.

## Transforming Shapes

Add another scene to your file:

```python
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

This demonstrates Manim's ability to "implement complicated and mathematically intensive animations with just a few lines of code."

## Positioning Mobjects

Use `next_to()` to position objects relative to each other:

```python
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square))
```

Parameters include a reference object, direction (`LEFT`, `UP`, `DOWN`, `RIGHT`), and buffer spacing.

## Using `.animate` Syntax

The `.animate` method animates changes to mobjects dynamically:

```python
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PINK, opacity=0.5))
```

When using `.animate`, "Manim takes a mobject's starting state and its ending state and interpolates the two," rather than applying changes before animation.

## Transform vs ReplacementTransform

- **Transform**: Modifies points and attributes of the original object into the target
- **ReplacementTransform**: Literally replaces one object with another on screen

Both achieve similar visual effects; choice depends on use case and reference management needs.

## Next Steps

After completing this quickstart, explore "Manim's Output Settings" tutorial for deeper understanding, or consult the Tutorials section and Reference Manual for comprehensive feature documentation.
