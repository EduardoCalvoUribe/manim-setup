# Manim's Output Settings

> Source: https://docs.manim.community/en/stable/tutorials/output_and_config.html

## Manim Output Folders

When executing a render command like `manim -pql scene.py SquareToCircle`, manim processes the specified scene file and generates organized output directories.

**Basic folder structure after rendering:**

```
project/
├─scene.py
└─media
  ├─videos
  |  └─scene
  |     └─480p15
  |        ├─SquareToCircle.mp4
  |        └─partial_movie_files
  ├─text
  └─Tex
```

The primary video output appears in `media/videos/scene/480p15/SquareToCircle.mp4`. The `media` folder contains all manim-generated files, with `media/videos` holding rendered animations organized by resolution and frame rate. The low-quality `-ql` flag produces 480×480 resolution at 15 frames per second.

**High-quality rendering:**

Using `-qh` instead of `-ql` renders at 1080p60 (1920×1080 resolution at 60 FPS), creating an additional `1080p60` subdirectory while preserving existing lower-quality versions.

**Capturing single frames:**

Adding the `-s` flag generates a final frame image in `media/images/scene/` alongside video files, providing quick scene previews without full rendering time.

## Sections

Scenes can be divided into sections using `self.next_section()` calls, with each section producing separate output videos.

**Section implementation example:**

```python
def construct(self):
    # play the first animations...
    # you don't need a section in the very beginning as it gets created automatically
    self.next_section()
    # play more animations...
    self.next_section("this is an optional name that doesn't have to be unique")
    # play even more animations...
    self.next_section("this is a section without any animations, it will be removed")
```

Each section must contain at least one animation to generate output. Sections without animations are automatically removed.

**Enabling section output:**

Use the `--save_sections` flag when rendering to create individual video files for each section:

```
manim --save_sections scene.py
```

**Generated section structure:**

```
media
├── images
│   └── simple_scenes
└── videos
    └── simple_scenes
        └── 480p15
            ├── ElaborateSceneWithSections.mp4
            ├── partial_movie_files
            │   └── ElaborateSceneWithSections
            │       ├── [various partial video files]
            │       └── partial_movie_file_list.txt
            └── sections
                ├── ElaborateSceneWithSections_0000.mp4
                ├── ElaborateSceneWithSections_0001.mp4
                ├── ElaborateSceneWithSections_0002.mp4
                └── ElaborateSceneWithSections.json
```

The accompanying JSON metadata file contains section details including name, video file reference, codec information, dimensions, frame rate, duration, and frame count.

**Skipping section animations:**

```python
def construct(self):
    self.next_section(skip_animations=True)
    # play some animations that shall be skipped...
    self.next_section()
    # play some animations that won't get skipped...
```

## Some Command Line Flags

**Scene selection:**

Specifying a scene name is optional when files contain a single `Scene` class. With multiple scenes, manim prompts for selection unless the `-a` flag renders all scenes automatically.

**Quality flags:**

| Flag | Resolution | FPS | Use case |
|------|-----------|-----|----------|
| `-ql` | 854×480 | 15 | Fastest, for prototyping |
| `-qm` | 1280×720 | 30 | Medium quality |
| `-qh` | 1920×1080 | 60 | High quality |
| `-qp` | 2560×1440 | 60 | 2K quality |
| `-qk` | 3840×2160 | 60 | 4K quality |

**Playback and display options:**

- `-p`: Automatically plays the rendered animation
- `-f`: Opens the file browser at the output location instead of playing
- Omitting both flags suppresses automatic action

**Output format:**

By default, manim generates `.mp4` files. The `--format gif` flag produces animated GIFs in the same directory with identical names but different extensions.
