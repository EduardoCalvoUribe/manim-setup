# Rendering Text and Formulas

> Source: https://docs.manim.community/en/stable/guides/using_text.html

## Overview

Manim offers two primary approaches for rendering text in animations:

1. **Pango (`text_mobject`)** — for simple, plain text rendering
2. **LaTeX (`tex_mobject`)** — for mathematical typesetting and complex formulas

---

## Text Without LaTeX

### Basic Text Rendering

The `Text` class uses the Pango library and supports multiple languages including non-English alphabets:

```python
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)
```

### MarkupText

`MarkupText` enables PangoMarkup formatting for more sophisticated styling:

```python
class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>',
            color=RED
        )
        self.add(text)
```

### Working with Text Objects

**Font Selection**: Install fonts system-wide; list available fonts with `manimpango.list_fonts()`.

**Slant and Weight**: Modify appearance using `slant` (NORMAL, ITALIC, OBLIQUE) and `weight` parameters.

**Colors**: Apply single colors or use `t2c` for character-specific coloring:

```python
class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World', t2c={'rl': RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)
```

**Gradients**: Use `gradient` for color transitions or `t2g` for targeted gradients.

**Line Spacing**: Control with the `line_spacing` parameter.

**Ligatures**: Disable with `disable_ligatures=True` to maintain one-to-one character-to-submobject mapping.

**Iteration**: Text objects behave like VGroups, allowing indexing and slicing for per-character manipulation.

---

## Text With LaTeX

### Basic LaTeX Rendering

```python
class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)
```

Use raw strings (`r'...'`) to avoid escaping special characters.

### MathTex

`MathTex` processes content in math mode by default within an `align*` environment:

```python
class MathTeXDemo(Scene):
    def construct(self):
        rtarrow = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        self.add(rtarrow)
```

### LaTeX Commands and Styling

Standard AMS math packages are supported. Apply keyword arguments like `color` to modify appearance:

```python
class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)
```

### Extra Packages

Load additional LaTeX packages via `TexTemplate`:

```python
class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)
```

### Substrings and Parts

Access parts by index or use `set_color_by_tex()` for exact string matching:

```python
class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex(r'$\bigstar$', RED)
        self.add(tex)
```

Use `substrings_to_isolate` to split formulas for targeting individual tokens:

```python
equation = MathTex(
    r"e^{x} = x^0 + x^1 + ...",
    substrings_to_isolate="x"
)
equation.set_color_by_tex("x", YELLOW)
```

Alternatively, use double braces to isolate parts:

```python
MathTex(r"{{ a^2 }} + {{ b^2 }}")
```

### Debug with index_labels()

The `index_labels()` function displays submobject indices for complex structures:

```python
class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)
        self.add(index_labels(text[0]))
        text[0][1:3].set_color(YELLOW)
        self.add(text)
```

### LaTeX Math Fonts

Use `TexFontTemplates` for predefined mathematical font styles:

```python
tex = Tex(
    r"$x^2 + y^2 = z^2$",
    tex_template=TexFontTemplates.french_cursive,
    font_size=144,
)
```

`TexTemplateLibrary` provides additional templates (e.g., `ctex` for Chinese).

### Aligning Formulae

Multiline formulas use LaTeX's `align*` environment with `&` for alignment:

```python
class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)
```
