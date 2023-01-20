from manim import *
import math
import numpy

class TransformedPlane(Scene):
    def construct(self):
        plane1 = NumberPlane(
            axis_config = {
                "stroke_color": GREY,
                "stroke_opacity": 0
            },
            background_line_style = {
                "stroke_color": GREY,
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
                "stroke_color": BLUE,
                "stroke_opacity": 1
            },
            background_line_style = {
                "stroke_color": BLUE,
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
        p2 = Dot().move_to([p2r, p2i, 0])
        l2 = Tex("$z_{2}$").add_updater(lambda x: x.move_to([p2r + .3, p2i + .3, 0]))
        p3 = Dot(color = BLUE).add_updater(lambda x: x.move_to([p3r(), p3i(), 0]))
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
        

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [("i" if i == 1 else ("-i" if i == -1 else f"{round(i)}i")) for i in val_range]