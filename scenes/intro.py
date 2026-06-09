from manim import *


class Intro(Scene):
    def construct(self):
        title = Text("Master Thesis", font_size=48)
        subtitle = Text("Your Name", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
