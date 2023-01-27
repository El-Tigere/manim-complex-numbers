from manim import *
from colorThemes import *

class Title(Scene):
    def construct(self):
        title = Tex("Mandelbrot")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))