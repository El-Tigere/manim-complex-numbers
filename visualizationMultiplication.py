from manim import *
import math
import numpy

class Multiplication(Scene):
    def construct(self):
        p1r = ValueTracker(1)
        p1i = ValueTracker(0)
        
        bgPlane = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config = {
                'stroke_color': GRAY
            },
            background_line_style= {
                'stroke_color': GREY,
                'stroke_opacity': 0.5
            }
        )
        fgPlane = always_redraw(lambda:
            NumberPlane(
                x_range=[-10, 10, 1],
                y_range=[-10, 10, 1],
                axis_config = {
                    'stroke_color': BLUE
                },
                background_line_style= {
                    'stroke_color': BLUE,
                    'stroke_opacity': 0.5
                }
            )
            .rotate(-numpy.arctan2(p1r.get_value(), p1i.get_value()))
            .scale(scale_factor = math.sqrt(p1r.get_value() ** 2 + p1i.get_value() ** 2))
        )
        point1 = always_redraw(lambda:
            Dot().move_to([p1r.get_value(), p1i.get_value(), 0])
        )
        self.play(Create(fgPlane))
        self.add(bgPlane)
        self.bring_to_back(bgPlane)
        self.play(Create(point1))
        self.wait(1)
        self.play(p1i.animate.set_value(2))
        self.play(p1r.animate.set_value(-2))
        self.play(p1i.animate.set_value(-3))
        self.play(p1i.animate.set_value(1), p1r.animate.set_value(2))
        self.wait(1)
        self.play(p1i.animate.set_value(0))
        self.play(p1r.animate.set_value(0))
        self.wait(3)