from manim import *

class main(Scene):
    def construct(self):
        text = MathTex(
            r"r S\frac{\partial F}{\partial S}",
            r"+",
            r"\frac{1}{2} \sigma^2 S^2\frac{\partial^2 F}{\partial S^2}",
            r"+",
            r"\frac{\partial F}{\partial t}",
            r"=",
            r"rF"
        )

        self.play(Write(text))
        
        self.wait(1)
