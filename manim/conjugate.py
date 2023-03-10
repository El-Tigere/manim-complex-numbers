from manim import *
from colorThemes import *
from axisLabels import *
import math
import numpy

class Title(Scene):
    def construct(self):
        title = Tex("Konjugation")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class Conjugate(Scene):
    COLORS = DARK_THEME
    def construct(self):
        # number planes and axis
        plane1 = NumberPlane(
            axis_config = {
                "stroke_color": self.COLORS["midground"],
                "stroke_opacity": 0
            },
            background_line_style = {
                "stroke_color": self.COLORS["midground"],
                "stroke_opacity": 0.5
            }
        )
        ax = Axes(
            x_length = 20,
            y_length = 20,
            x_range = [-10, 10, 1],
            y_range = [-10, 10, 1],
            y_axis_config = {
                "scaling": ImaginaryBase()
            }
        ).add_coordinates()
        plane2 = NumberPlane(
            axis_config = {
                "stroke_color": self.COLORS["highlight"],
                "stroke_opacity": 1
            },
            background_line_style = {
                "stroke_color": self.COLORS["highlight"],
                "stroke_opacity": 0.5
            }
        ).rotate(-numpy.arctan2(1, 2)).scale(math.sqrt(5))
        
        # points
        p1 = Dot().move_to([1, 2, 0])
        l1 = Tex("a+bi").move_to([1.75, 2, 0])
        p2 = Dot().move_to([1, -2, 0])
        l2 = Tex("a-bi").move_to([1.75, -2, 0])
        p3 = Dot().move_to([5, 0, 0])
        
        # arrows
        a1 = Arrow(start = [0, 0, 0], end = [1, 2, 0], stroke_width = 5, buff = 0.05)
        a2 = Arrow(start = [1, 2, 0], end = [3, 1, 0], stroke_width = 5, buff = 0.05)
        a3 = Arrow(start = [3, 1, 0], end = [5, 0, 0], stroke_width = 5, buff = 0.05)
        
        # animation:
        
        # create complex plane
        self.play(Create(plane1), Create(ax))
        self.wait(1)
        
        # create point
        self.play(Create(p1), Create(l1))
        self.play(Create(p2), Create(l2))
        self.wait(1)
        
        # highlight x-axis
        self.play(Indicate(ax.get_x_axis(), color = self.COLORS["highlight"]))
        self.wait(1)
        
        # create transformed Plane
        self.bring_to_back(plane2)
        self.play(Create(plane2))
        self.wait(1)
        
        # create arrows
        self.play(Create(a1))
        self.play(Create(a2))
        self.play(Create(a3))
        self.play(Create(p3))
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(p1), FadeOut(l1), FadeOut(p2), FadeOut(l2), FadeOut(plane2), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(p3))
        self.wait(1)
        self.play(FadeOut(plane1), FadeOut(ax))