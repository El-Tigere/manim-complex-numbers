from manim import *
from colorThemes import *
import absoluteValue
import multiplication
import conjugate
import division

class ComplexNumbers(Scene):
    COLORS = LIGHT_THEME
    def construct(self):
        self.camera.background_color = self.COLORS["background"]
        Tex.set_default(color = self.COLORS["foreground"])
        Mobject.set_default(color = self.COLORS["foreground"])
        Dot.set_default(color = self.COLORS["foreground"])
        
        self.wait(1)
        absoluteValue.Title.construct(self)
        absoluteValue.Abs.construct(self)
        multiplication.Title.construct(self)
        multiplication.TransformedPlane.construct(self)
        multiplication.Multiplication.construct(self)
        multiplication.Examples.construct(self)
        conjugate.Title.construct(self)
        conjugate.Conjugate.construct(self)
        division.Title.construct(self)
        division.TransformedPlane.construct(self)
        self.wait(3)
