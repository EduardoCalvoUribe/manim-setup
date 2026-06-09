# Manim's Building Blocks

> Source: https://docs.manim.community/en/stable/tutorials/building_blocks.html

## Core Concepts

Manim provides three essential building blocks:

1. **Mobjects** (mathematical objects) - displayable entities
2. **Animations** - procedures that interpolate between mobject states
3. **Scenes** - containers that manage mobjects and animations

## Mobjects

Mobjects are basic animation elements derived from the `Mobject` class. Examples include shapes like `Circle`, `Arrow`, and `Rectangle`, as well as complex constructs like `Axes`, `FunctionGraph`, and `BarChart`.

The `VMobject` (Vectorized Mobject) subclass uses vector graphics and forms the basis for most predefined classes.

### Creating and Displaying

Add mobjects to scenes using the `add()` method within a `Scene.construct()` method. Remove them with `remove()`.

### Positioning Methods

- `shift()` - relative movement
- `move_to()` - absolute positioning
- `next_to()` - position relative to another mobject
- `align_to()` - align borders using bounding boxes

### Styling

Apply visual properties using:

- `set_stroke()` - border styling (VMobjects only)
- `set_fill()` - interior styling with opacity (VMobjects only)
- `set_color()` - general coloring (all Mobjects)

### Z-Order

"The order of the arguments of `add()` determines the order that the mobjects are displayed on the screen, with the left-most arguments being put in the back."

## Animations

Animations interpolate mobject properties over time using the `play()` method.

### Built-in Animations

Examples include `FadeIn`, `FadeOut`, and `Rotate`, each modifying different properties.

### Animate Property

The `animate` property animates method calls on mobjects:

```python
self.play(square.animate.set_fill(WHITE))
self.play(square.animate.shift(UP).rotate(PI / 3))
```

### Run Time Control

Animations default to one second. Use the `run_time` parameter to adjust duration.

### Custom Animations

Extend the `Animation` class and override `interpolate_mobject(alpha)`, which receives values from 0 to 1 representing animation progress. This enables creating specialized interpolation behaviors.

### Mobject Coordinates

Access positional data using methods like:

- `get_center()`
- `get_top()`
- `get_start()`
- `get_end()`
- `point_from_proportion()`

### Transform Animation

Transform one mobject into another using the `Transform` class. Point alignment may require using `numpy.roll()` to prevent distortion.

## Scenes

The `Scene` class orchestrates all animation elements. Key operations:

| Method | Description |
|--------|-------------|
| `add()` | Display mobjects |
| `remove()` | Hide mobjects |
| `play()` | Execute animations |
| `wait()` | Pause playback |
| `construct()` | Required method containing all scene code |

Multiple `Scene` subclasses can exist in one file for batch rendering.
