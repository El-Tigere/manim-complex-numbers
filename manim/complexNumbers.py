from manim import *
import absoluteValue
import multiplication
import conjugate
import division

class ComplexNumbers(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.wait(1)
        #absoluteValue.Title.construct(self)
        #absoluteValue.Abs.construct(self)
        #multiplication.Title.construct(self)
        #multiplication.TransformedPlane.construct(self)
        #multiplication.Multiplication.construct(self)
        #multiplication.Examples.construct(self)
        conjugate.Title.construct(self)
        conjugate.Conjugate.construct(self)
        division.Title.construct(self)
        division.TransformedPlane.construct(self)
        self.wait(3)
