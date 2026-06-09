# Configuration

> Source: https://docs.manim.community/en/stable/guides/configuration.html

Manim offers "an extensive configuration system that allows it to adapt to many different use cases." Configuration can be set through three primary methods: command-line arguments, the ManimConfig class, and configuration files.

## Command-Line Configuration

The most commonly used command is `manim render`, which renders scenes to output files. Basic usage:

```
manim [OPTIONS] FILE [SCENES]
```

### Common Flags

| Flag | Description |
|------|-------------|
| `-qm` | Medium quality rendering |
| `-p` | Preview the rendered video after completion |
| `-sqh` | Save only the last frame in high quality |
| `-o` | Specify output filename |
| `--format=gif` | Save as GIF instead of MP4 |
| `-n 0,10` | Render only animations 0–10 |

### Quality Levels

The `-q` flag supports these presets:

| Preset | Resolution | FPS |
|--------|-----------|-----|
| `l` | 854×480 | 15 |
| `m` | 1280×720 | 30 |
| `h` | 1920×1080 | 60 |
| `p` | 2560×1440 | 60 |
| `k` | 3840×2160 | 60 |

## The ManimConfig Class

The global `config` object is an instance of `ManimConfig` and can be accessed using attribute or dictionary syntax:

```python
from manim import *
config.background_color = WHITE
config["background_color"] = WHITE  # Also valid
```

The config maintains internal consistency — changing one property affects related properties. For example, "setting `frame_y_radius` will affect `frame_height`."

## Configuration Files

### Folder-Wide Config

Create a `manim.cfg` file in the same directory as your scene script. The file must begin with `[CLI]`:

```ini
[CLI]
# Configuration options
output_file = myscene
save_as_gif = True
background_color = WHITE
```

Options use long names (e.g., `background_color` rather than `-c`). Lines beginning with `#` are ignored.

### User-Wide Config

A user-wide configuration applies across all Manim projects:

| OS | Path |
|----|------|
| Windows | `UserDirectory/AppData/Roaming/Manim/manim.cfg` |
| macOS | `UserDirectory/.config/manim/manim.cfg` |
| Linux | `UserDirectory/.config/manim/manim.cfg` |

## Configuration Precedence

When multiple config sources exist, they follow this cascading order (lowest to highest priority):

1. Library-wide config file
2. User-wide config file (if present)
3. Folder-wide config file OR custom config file (via `--config_file`)
4. Command-line flags
5. Programmatic changes after initialization

"If they are incompatible, the folder-wide file takes precedence" over the user-wide file.

## Configuration Order of Operations

When Manim is imported as a module:

1. Library-wide config loads
2. User-wide and folder-wide configs load (if present)
3. Files parse into a ConfigParser object
4. Logger instantiates and configures
5. ManimConfig instantiates
6. Parser feeds into config via `digest_parser()`
7. Logger and config expose to user

Command-line invocation adds these steps:

1. CLI flags parse and feed into config
2. Optional custom config file processing
3. Remaining CLI flags process

## All Config Options

Manim supports approximately 50 configuration options, including: `aspect_ratio`, `background_color`, `frame_height`, `frame_rate`, `output_file`, `pixel_height`, `pixel_width`, `preview`, `quality`, `save_as_gif`, `transparent`, `verbosity`, and many others related to rendering, output directories, and display settings.

## Accessing CLI Help

```bash
manim --help          # main help
manim render --help   # render-specific help
```

Individual subcommands (`cfg`, `plugins`, `init`) each have their own help pages accessible via the same `--help` flag.
