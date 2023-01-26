from manim import *
from colorThemes import *

class Title(Scene):
    def construct(self):
        title = Tex("Betrag")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class Abs(Scene):
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
        
        # point
        p1 = Dot().move_to([3, 2, 0])
        l1 = Tex("a+bi").move_to([3.75, 2, 0])
        
        # triangle
        arrow1 = DoubleArrow([0, 0, 0], [3, 2, 0], stroke_width = 5, buff = 0).set_color(self.COLORS["highlight"])
        line1 = DashedLine([0, 0, 0], [3, 0, 0], dash_length = 0.2, stroke_width = 5).set_color(self.COLORS["highlight"])
        line2 = DashedLine([3, 0, 0], [3, 2, 0], dash_length = 0.2, stroke_width = 5).set_color(self.COLORS["highlight"])
        
        # triangle labels
        l2 = Tex("a").move_to([1.5, -0.25, 0]).set_color(self.COLORS["highlight"])
        l3 = Tex("b").move_to([3.25, 1, 0]).set_color(self.COLORS["highlight"])
        l4 = Tex("$\\sqrt{a^2+b^2}$").move_to([0.75, 1.5, 0]).set_color(self.COLORS["highlight"])
        
        # animation:
        
        # create complex plane
        self.play(Create(plane1), Create(ax))
        self.wait(1)
        
        # create point
        self.play(Create(p1), Create(l1))
        self.play(Create(arrow1))
        self.wait(1)
        
        # split a and b to triangle sides
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(Create(l2), Create(l3))
        self.wait(1)
        
        # create hypotenuse label
        self.play(Create(l4))
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(p1), FadeOut(l1), FadeOut(arrow1), FadeOut(line1), FadeOut(line2), FadeOut(l2), FadeOut(l3), FadeOut(l4))
        self.wait(1)
        self.play(FadeOut(plane1), FadeOut(ax))

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [("i" if i == 1 else ("-i" if i == -1 else f"{round(i)}i")) for i in val_range]