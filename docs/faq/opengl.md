# FAQ: OpenGL Rendering

> Source: https://docs.manim.community/en/stable/faq/opengl.html

---

## Resources for OpenGL Renderer Usage

The official documentation currently lacks coverage of base classes like `OpenGLMobject` and `OpenGLVMobject`, or specialized classes like `OpenGLSurface`. However, documentation exists as docstrings in the [source code repository](https://github.com/ManimCommunity/manim/tree/main/manim/mobject/opengl).

Additionally, a community user guide by *aquabeam* provides practical introductory material for working with the OpenGL renderer.

---

## Resolving `sqlite3.ProgrammingError` with Interactive OpenGL Scenes

When running interactive scenes using `--renderer=opengl` and `Scene.interactive_embed`, a `sqlite3.ProgrammingError` may occur due to compatibility issues with recent IPython versions.

**Solution:** Downgrade IPython to version 8.0.1:

```bash
pip install IPython==8.0.1
```

This downgrade has been observed to resolve the error in practice.
