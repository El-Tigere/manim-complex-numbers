from manim import *
import math
import numpy

class Title(Scene):
    def construct(self):
        title = Tex("Multiplikation")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

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
        # number planes and axis
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
        p1r = ValueTracker(1)
        p1i = ValueTracker(0)
        p2r = 2
        p2i = 1
        p3r = lambda: p1r.get_value() * p2r - p1i.get_value() * p2i
        p3i = lambda: p1r.get_value() * p2i + p1i.get_value() * p2r
        
        # points p1, p2, p3 and labels
        p1 = Dot().add_updater(lambda x: x.move_to([p1r.get_value(), p1i.get_value(), 0]))
        l1 = Tex("$z_{1}$").add_updater(lambda x: x.move_to([p1r.get_value() + .3, p1i.get_value() + .3, 0]))
        p2 = Dot().move_to([p2r, p2i, 0])
        l2 = Tex("$z_{2}$").add_updater(lambda x: x.move_to([p2r + .3, p2i + .3, 0]))
        p3 = Dot(color = BLUE).add_updater(lambda x: x.move_to([p3r(), p3i(), 0]))
        l3 = Tex("$z_{3}$").add_updater(lambda x: x.move_to([p3r() + .3, p3i() - .3, 0]))
        
        # path of p3
        path = TracedPath(traced_point_func = p3.get_center, stroke_color = BLUE)
        
        # transformed plane labels
        tpl =  VGroup()
        tpl.add(Tex("1").set_color(BLUE).move_to([2 - 0.2, 1 - 0.4, 0]))
        tpl.add(Tex("-1").set_color(BLUE).move_to([-2 - 0.2, -1 - 0.4, 0]))
        tpl.add(Tex("i").set_color(BLUE).move_to([-1 - 0.2, 2 - 0.4, 0]))
        tpl.add(Tex("-i").set_color(BLUE).move_to([1 - 0.2, -2 - 0.4, 0]))
        
        # animation:
        
        # create complex plane and p1 and p2
        self.play(Create(plane1), Create(ax))
        self.play(Create(p1), Create(l1))
        self.play(Create(p2), Create(l2))
        self.wait(1)
        
        # create multiplication result (p3)
        self.play(Create(p3), Create(l3))
        self.add(path)
        self.bring_to_back(path)
        self.wait(1)
        
        # move p1 on the real axis
        self.play(p1r.animate.set_value(0))
        self.wait(1)
        self.play(p1r.animate.set_value(2))
        self.wait(1)
        self.play(p1r.animate.set_value(-2))
        self.wait(1)
        
        # move p1 on the imaginary axis
        self.play(p1r.animate.set_value(0))
        self.play(p1i.animate.set_value(1))
        self.wait(1)
        self.play(p1i.animate.set_value(2))
        self.play(p1i.animate.set_value(-2))
        self.play(p1i.animate.set_value(0))
        self.wait(1)
        
        # create transformed plane
        self.play(Create(plane2))
        self.remove(path)
        self.play(FadeOut(p1), FadeOut(l1), FadeOut(p3), FadeOut(l3))
        self.wait(1)
        
        # show where 1, -1, i and -1 are on the transformed plane
        self.play(Create(tpl))
        self.wait(1)
        
        # remove transformed plane
        self.play(FadeOut(plane2), FadeOut(tpl))
        self.play(FadeOut(p2), FadeOut(l2))
        self.wait(1)

class Examples(Scene):
    def construct(self):
        # number planes and axis
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
        
        # points
        p1 = Dot().move_to([1, 0.5, 0])
        p2 = Dot().move_to([-3, 2, 0])
        p3 = Dot().set_color(BLUE).move_to([-4, 0.5, 0])
        
        # arrows (badly organized)
        a1 = Arrow(start = [0, 0, 0], end = [1, 0.5, 0], buff = 0.05)
        a2 = Arrow(start = [0, 0, 0], end = [-1, -0.5, 0], buff = 0.05).set_color(BLUE)
        a3 = Arrow(start = [-1, -0.5, 0], end = [-2, -1, 0], buff = 0.05).set_color(BLUE)
        a4 = Arrow(start = [-2, -1, 0], end = [-3, -1.5, 0], buff = 0.05).set_color(BLUE)
        a5 = Arrow(start = [-3, -1.5, 0], end = [-3.5, -0.5, 0], buff = 0.05).set_color(BLUE)
        a6 = Arrow(start = [-3.5, -0.5, 0], end = [-4, 0.5, 0], buff = 0.05).set_color(BLUE)
        
        # animations:
        
        # add complex plane (no animation)
        self.add(plane1, ax)
        self.wait(1)
        
        # create example factors
        self.play(Create(p1), Create(p2))
        self.wait(1)
        
        # create arrows
        self.play(Create(a1))
        self.wait(1)
        self.play(Create(a2))
        self.play(Create(a3))
        self.play(Create(a4))
        self.wait(1)
        self.play(Create(a5))
        self.play(Create(a6))
        self.wait(1)
        
        # show p3 (result)
        self.play(Create(p3))
        self.wait(1)
        

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [("i" if i == 1 else ("-i" if i == -1 else f"{round(i)}i")) for i in val_range]