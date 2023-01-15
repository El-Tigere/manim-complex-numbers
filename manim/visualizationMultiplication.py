from manim import *
import math
import numpy

class Formula(Scene):
    def construct(self):
        formula1 = Tex("(a + bi) * (c + di) = (ac - bd) + (bc + ad)i")
        self.play(Create(formula1))
        self.wait(3)
        self.play(FadeOut(formula1, shift = UP))

label1Text = ""
label1Save = None

class Multiplication(Scene):
    def construct(self):
        p1r = ValueTracker(1)
        p1i = ValueTracker(0)
        
        bgPlane = NumberPlane(
            x_range = [-10, 10, 1],
            y_range = [-10, 10, 1],
            axis_config = {
                "stroke_color": GRAY
            },
            background_line_style = {
                "stroke_color": GREY,
                "stroke_opacity": 0.5
            }
        )
        fgPlane = always_redraw(lambda:
            NumberPlane(
                x_range = [-10, 10, 1],
                y_range = [-10, 10, 1],
                axis_config = {
                    "stroke_color": BLUE
                },
                background_line_style = {
                    "stroke_color": BLUE,
                    "stroke_opacity": 0.5
                }
            )
            .rotate(-numpy.arctan2(p1r.get_value(), p1i.get_value()))
            .scale(scale_factor = math.sqrt(p1r.get_value() ** 2 + p1i.get_value() ** 2))
        )
        
        point0 = Dot().move_to([0, 0, 0])
        point1 = always_redraw(lambda:
            Dot().move_to([p1r.get_value(), p1i.get_value(), 0])
        )
        def getLabel1():
            global label1Text, label1Save
            newText = f"{round(p1r.get_value(), 1)}+{round(p1i.get_value(), 1)}i"
            if(label1Save is None or newText != label1Text):
                label1Text = newText
                label1Save = Tex(label1Text)
            return label1Save.move_to([p1r.get_value(), p1i.get_value() - 0.4, 0])
        label1 = always_redraw(getLabel1)
        
        self.play(Create(fgPlane))
        self.add(bgPlane)
        self.bring_to_back(bgPlane)
        self.play(Create(point0))
        self.play(Create(point1), Create(label1))
        self.wait(1)
        self.play(p1i.animate.set_value(2))
        self.play(p1r.animate.set_value(-2))
        self.play(p1i.animate.set_value(-3))
        self.play(p1i.animate.set_value(1), p1r.animate.set_value(2))
        self.wait(3)

class TransformedPlane(Scene):
    def construct(self):
        plane = NumberPlane(
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
            x_axis_config = {
                "stroke_color": BLUE,
                "stroke_opacity": 1
            },
            y_axis_config = {
                "scaling": ImaginaryBase(scale_factor = 1, custom_labels = True),
                "stroke_color": BLUE,
                "stroke_opacity": 1
            }
        ).add_coordinates()
        p1 = Dot().move_to([1, 0, 0])
        
        self.add(plane, ax, p1)
        self.wait(1)

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [f"{round(i)}i" for i in val_range]