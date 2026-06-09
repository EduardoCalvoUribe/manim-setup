# FAQ: Installation

> Source: https://docs.manim.community/en/stable/faq/installation.html

---

## Why are there different versions of Manim?

Manim was originally created by Grant Sanderson as a personal project for his YouTube channel, 3Blue1Brown. As the channel gained popularity, others wanted to use it for their own projects.

In late 2019, Grant developed faster OpenGL rendering in a new branch called `shaders`. By mid-2020, developers forked this into the community edition, which is now documented on this website. In early 2021, Grant merged the shaders branch into master, creating `manimgl`. The earlier version, sometimes called `ManimCairo`, is primarily useful for rendering Grant's old videos.

### Summary of Versions

| Version | PyPI Package | Notes |
|---------|-------------|-------|
| **Manim / ManimCE** | `manim` | Community-maintained; documented here; recommended for beginners |
| **ManimGL** | `manimgl` | Grant Sanderson's latest; experimental features; undocumented breaking changes |
| **ManimCairo** | `manimlib` | Pre-OpenGL; only for rendering legacy 3Blue1Brown projects |

---

## Which version should I use?

The community-maintained version is recommended, especially for beginners, because it offers "stability, better testing and documented resources, and quicker community contributions."

Use **ManimGL** if you prioritize using Grant Sanderson's exact version over documentation and stability. Use **ManimCairo** only for rendering pre-2019 3Blue1Brown projects.

---

## How can I tell which version a scene was written for?

Import statements reveal the target version:

| Import | Version |
|--------|---------|
| `from manim import *` or `import manim as mn` | Community-maintained (ManimCE) |
| `import manimlib` or `from manimlib import *` | ManimGL |
| `from manimlib.imports import *` or `from big_ol_pile_of_manim_imports import *` | Early ManimCairo |

---

## How do I know which version of Manim I have installed?

Run `manim` in your terminal. For the community version, the first output line reads "Manim Community \<version number\>".

Alternatively, run `python -m pip list` to check installed packages for `manim` or `manimgl`.

---

## I am following a YouTube video guide to install Manim, but some step fails. What do I do?

Many YouTube installation guides are severely outdated and cannot be easily updated. Use the written installation guide instead. If preferring video format, verify the creator has a recent version available, or contact them directly.

---

## Why does ManimPango fail to install when running `pip install manim`?

This typically indicates pip cannot use pre-built wheels for `manimpango`. Report your architecture via Discord or GitHub issues. Ensure all build requirements from ManimPango's README are installed, particularly in the BUILDING section.

---

## I am using Windows and get the error `X is not recognized as an internal or external command`

If following local installation instructions without activating the virtual environment, use `uv run manim ...` instead of just `manim`. Otherwise, PATH variables may need adjustment. Try prepending `python -m` to commands (e.g., `python -m manim` instead of `manim`).

---

## I have tried using Chocolatey (`choco install manimce`) to install Manim, but it failed!

Ensure administrator permissions when running the command. Review Chocolatey's output for mentioned `.log` files containing failure details. Submit logs and relevant information to the community for assistance.

---

## On Windows, when typing `python` or `python3` the Windows Store opens. Can I fix this?

Yes, follow these steps:

1. Open Windows Settings
2. Navigate to Apps and Features
3. Find application execution aliases
4. Disable the problematic `python` and/or `python3` aliases

---

## I am using Anaconda and get an `ImportError` mentioning that some Symbol is not found.

Anaconda environments include preinstalled `cairo` incompatible with Manim's `pycairo` version. Fix by running:

```bash
conda install -c conda-forge pycairo
```

---

## How can I fix the error that `manimpango/cmanimpango.c` could not be found?

This occurs when systems must build ManimPango locally due to unavailable compatible PyPI versions. Try installing Cython first:

```bash
pip3 install Cython
```

Then reinstall Manim. If problems persist, verify all build dependencies from ManimPango's README are installed, then contact the community through Getting Help resources.
