from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello, Manim in Codespaces!")
        self.play(Write(text))
        self.wait(1)