from manim import *
from colorThemes import *
from axisLabels import *
import math
import numpy

class Title(Scene):
    def construct(self):
        title = Tex("Durch 0 teilen")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class TransformedPlane(Scene):
    COLORS = DARK_THEME
    def construct(self):
        p1r = ValueTracker(1)
        p1i = ValueTracker(0)
        
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
        plane2 = always_redraw(lambda:
            NumberPlane(
                x_range = [-10, 10, 1],
                y_range = [-10, 10, 1],
                axis_config = {
                    "stroke_color": self.COLORS["highlight"]
                },
                background_line_style = {
                    "stroke_color": self.COLORS["highlight"],
                    "stroke_opacity": 0.5
                }
            )
            .rotate(-numpy.arctan2(p1r.get_value(), p1i.get_value()))
            .scale(scale_factor = math.sqrt(p1r.get_value() ** 2 + p1i.get_value() ** 2))
        )
        
        # points
        p1 = always_redraw(lambda:
            Dot().move_to([p1r.get_value(), p1i.get_value(), 0])
        )
        p2 = Dot().move_to([3, -2, 0]).set_color(self.COLORS["highlight"])
        l2 = Tex("$\infty?$").move_to([3, -1.6, 0])
        
        # animations:
        
        # create complex plane
        self.play(Create(plane1), Create(ax))
        self.wait(1)
        
        # create factor point and transformed plane
        self.play(Create(p1))
        self.play(Create(plane2))
        self.wait(1)
        
        # move factor point to zero
        self.play(p1r.animate.set_value(0))
        self.remove(plane2)
        self.wait(1)
        
        # create example point
        self.play(Create(p2))
        self.wait(1)
        self.play(Create(l2))
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(l2))
        self.wait(1)
        self.remove(plane1, ax)

class InfinityDirection(Scene):
    COLORS = DARK_THEME
    def construct(self):
        p1r = ValueTracker(1)
        p1i = ValueTracker(0)
        
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
                "scaling": ImaginaryBase(scale_factor = 1, custom_labels = True)
            }
        ).add_coordinates()
        plane2 = always_redraw(lambda:
            NumberPlane(
                x_range = [-10, 10, 1],
                y_range = [-10, 10, 1],
                axis_config = {
                    "stroke_color": self.COLORS["highlight"]
                },
                background_line_style = {
                    "stroke_color": self.COLORS["highlight"],
                    "stroke_opacity": 0.5
                }
            )
            .rotate(-numpy.arctan2(p1r.get_value(), p1i.get_value()))
            .scale(scale_factor = math.sqrt(p1r.get_value() ** 2 + p1i.get_value() ** 2))
        )
        
        # points
        p1 = always_redraw(lambda:
            Dot().move_to([p1r.get_value(), p1i.get_value(), 0])
        )
        
        # animations:
        
        # add complex plane (no animation)
        self.add(plane1, ax)
        
        # create factor point and transformed plane
        self.play(Create(p1))
        self.play(Create(plane2))
        self.wait(1)
        
        # move factor point around and to zero
        self.play(p1r.animate.set_value(0), p1i.animate.set_value(1))
        self.play(p1r.animate.set_value(-1))
        self.play(p1r.animate.set_value(0), p1i.animate.set_value(0))
        self.remove(plane2)
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(p1))
        self.wait(1)
        self.play(FadeOut(plane1), FadeOut(ax))