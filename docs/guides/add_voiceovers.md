# Adding Voiceovers to Videos

> Source: https://docs.manim.community/en/stable/guides/add_voiceovers.html

## Overview

"Creating a full-fledged video with voiceovers is a bit more involved than creating purely visual Manim scenes." Traditionally, this required using external video editing software after rendering, a process that could be tedious and time-consuming.

## Solution: Manim Voiceover Plugin

To simplify this workflow, the Manim community developed **Manim Voiceover**, a dedicated plugin for integrating audio directly into scenes through Python code.

### Installation

```bash
pip install "manim-voiceover[azure,gtts]"
```

For detailed installation instructions, consult the [official installation documentation](https://voiceover.manim.community/en/latest/installation.html).

## Key Features

The plugin enables developers to:

- Integrate voiceovers into Manim videos directly through Python, eliminating the need for external video editors
- Record custom voiceovers using a microphone via a command-line interface during the rendering process
- Use auto-generated AI voices from various free and paid text-to-speech services for animation development

## Basic Implementation

The API works by inheriting from `VoiceoverScene` instead of the standard `Scene` class. Animations are synchronized with audio using context managers that automatically calculate timing:

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class RecorderExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())
        circle = Circle()

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)
```

The `tracker.duration` automatically provides the audio length, synchronizing animations accordingly.

## Getting Started

- **Quick Start Guide**: https://voiceover.manim.community/en/latest/quickstart.html
- **Example Gallery**: https://voiceover.manim.community/en/latest/examples.html
