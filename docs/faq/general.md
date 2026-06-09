# FAQ: General Usage

> Source: https://docs.manim.community/en/stable/faq/general.html

---

## Why does Manim say that "there are no scenes inside that module"?

Two primary causes exist for this error:

1. **Unsaved file changes** — You edited your `Scene` class but forgot to save
2. **Wrong file passed** — You accidentally specified an incorrect filename

The error also commonly occurs when mixing Manim versions. If you're using community version code (containing `from manim import *`) but the `manimgl` executable has overwritten your `manim` command, this error appears.

**Verification:** Run `manim --version`. Community version output starts with "Manim Community v...". If not, you're running `manimgl`.

**Solutions:**
- Reinstall `manim`
- Use the `manimce` executable instead
- Call via Python module: `python -m manim`

---

## No matter what code I put in my file, Manim only renders a black frame. Why?

Verify the method containing your code follows the standard pattern and is named `construct`:

```python
class MyAwesomeScene(Scene):
    def construct(self):
        # your animation code
```

Manim won't execute any code unless the method is correctly named `construct` or explicitly called from within it.

---

## What are the default measurements for Manim's scene?

The scene measures **8 units in height** with a **16:9 aspect ratio**, yielding approximately **14.22 units in width** (8 × 16/9).

The origin sits at the scene's center. The upper left corner has coordinates approximately `[-7.11, 4, 0]`.

---

## How do I find out which keyword arguments I can pass when creating a Mobject?

Classes like `Circle` document specific arguments (`radius`, `color`) and include a catchall `**kwargs` parameter passing unprocessed arguments to parent classes.

Trace through parent classes in the inheritance chain to discover available arguments. Key styling parameters are documented in base classes `VMobject` and `Mobject`.

---

## Can Manim render a video with transparent background?

Yes, using the `-t` flag (or `--transparent`). Note: "Standard video formats don't support transparency, so Manim outputs `.mov` instead of `.mp4`" when using this flag.

Alternative formats: `--format=webm` or `--format=gif`

---

## I have watched a video where a creator ran command X, but it does not work for me. Why?

The video likely used an older Manim version. Either adopt that same version or modify the code accordingly (method names may have changed). Check the video description for compatibility notes.

---

## When using `Tex` or `MathTex`, some letters are missing. How can I fix this?

Rebuild LaTeX fonts by running:

```bash
fmtutil -sys --all
```

Consult your LaTeX distribution's documentation for additional guidance.

---

## I want to translate some code from `manimgl` to `manim`, what do I do with `CONFIG` dictionaries?

Community version dropped `CONFIG` dictionaries in v0.2.0 (January 2021).

**Simple cases:** Set attributes directly:

```python
class NewStyle(Scene):
    a = 1
    b = 2
```

**Inheritance cases:** Add arguments to `__init__`:

```python
class Thing(VMobject):
    def __init__(self, stroke_color=RED, fill_opacity=0.7,
                 my_awesome_argument=42, **kwargs):
        self.my_awesome_argument = my_awesome_argument
        super().__init__(stroke_color=stroke_color,
                        fill_opacity=fill_opacity, **kwargs)
```

---

## My installation does not support converting PDF to SVG, help?

**Step 1:** Verify `dvisvgm` version is at least 2.4:

```bash
dvisvgm --version
```

**Step 2:** Check PostScript support:

```bash
dvisvgm -l
```

Output should contain "ps dvips PostScript specials". If missing, check for `--libgs=filename` flag support:

```bash
dvisvgm -h
```

**Step 3:** If `--libgs` exists, locate the Ghostscript library (`libgs.so`, `gsdll32.dll`, `gsdll64.dll`, or `libgsl.dylib` depending on your OS).

**Step 4:** Set the environment variable:

```bash
export LIBGS=<path including filename>  # Linux/macOS
set LIBGS=<path including filename>     # Windows
```

Verify with:

```bash
dvisvgm -V1
```

Consult the [dvisvgm FAQ](https://dvisvgm.de/FAQ/) for additional troubleshooting.

---

## Where can I find more resources for learning Manim?

The Manim Community Discord server maintains a `#beginner-resources` channel with curated learning links. Join at https://manim.community/discord and contribute resources you discover.
