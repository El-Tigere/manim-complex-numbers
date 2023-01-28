from manim import *
from colorThemes import *
from axisLabels import *
import math
import numpy

class Title(Scene):
    def construct(self):
        title = Tex("Division")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class TransformedPlane(Scene):
    COLORS = DARK_THEME
    def construct(self):
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
                "scaling": ImaginaryBase(scale_factor = 1, custom_labels = True)
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
        ).rotate(-numpy.arctan2(2, 1)).scale(math.sqrt(5))
        
        # coordinates of p1, p2 and p3
        p1r = ValueTracker(4)
        p1i = ValueTracker(2)
        p2r = 2
        p2i = 1
        p3r = lambda: (p1r.get_value() * p2r + p1i.get_value() * p2i) / (p2r * p2r + p2i * p2i)
        p3i = lambda: (p1i.get_value() * p2r - p1r.get_value() * p2i) / (p2r * p2r + p2i * p2i)
        
        # points p1, p2, p3 and labels
        p1 = Dot().add_updater(lambda x: x.move_to([p1r.get_value(), p1i.get_value(), 0]))
        l1 = Tex("$z_{1}$").add_updater(lambda x: x.move_to([p1r.get_value() + .3, p1i.get_value() + .3, 0]))
        p2 = Dot(color = self.COLORS["highlight"]).move_to([p2r, p2i, 0])
        l2 = Tex("$z_{2}$").add_updater(lambda x: x.move_to([p2r + .3, p2i + .3, 0]))
        p3 = Dot().add_updater(lambda x: x.move_to([p3r(), p3i(), 0]))
        l3 = Tex("$z_{3}$").add_updater(lambda x: x.move_to([p3r() + .3, p3i() - .3, 0]))
        
        # animation:
        
        # create complex plane
        self.play(Create(plane1), Create(ax))
        self.wait(1)
        
        # create divisor point and transformed plane
        self.play(Create(plane2))
        self.play(Create(p2), Create(l2))
        self.wait(1)
        
        # create dividend and result
        self.play(Create(p1), Create(l1))
        self.play(Create(p3), Create(l3))
        self.wait(1)
        
        # move dividend
        self.play(p1r.animate.set_value(4.5), p1i.animate.set_value(1))
        self.wait(1)
        self.play(p1r.animate.set_value(3), p1i.animate.set_value(-1))
        self.wait(1)
        self.play(p1r.animate.set_value(4), p1i.animate.set_value(-3))
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(plane2), FadeOut(p1), FadeOut(l1), FadeOut(p2), FadeOut(l2), FadeOut(p3), FadeOut(l3))
        self.wait(1)
        self.play(FadeOut(plane1), FadeOut(ax))