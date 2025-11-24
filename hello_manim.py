from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Tex("Hello, $x+1$ Manim in Codespaces! $x$")
        self.play(Write(text))
        self.wait(1)

        