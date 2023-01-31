from manim import *
from colorThemes import *
from axisLabels import *

class Title(Scene):
    def construct(self):
        title = Tex("Die komplexe Ebene")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class ComplexPlane(Scene):
    COLORS = DARK_THEME
    def construct(self):
        # natural points
        points1 = [Dot().move_to([x, 0, 0]) for x in range(0, 8)]
        points1Group = VGroup()
        for p in points1:
            points1Group.add(p)
        labels1 = [Tex(str(x)).move_to([x, -0.36, 0]) for x in range(0, 8)]
        labels1Group = VGroup()
        for l in labels1:
            l.font_size = 36
            labels1Group.add(l)
        
        # not real integer points
        points2 = [Dot().move_to([x, 0, 0]) for x in range(-8, 0)]
        points2Group = VGroup()
        for p in points2:
            points2Group.add(p)
        labels2 = [Tex(str(x)).move_to([x, -0.36, 0]) for x in range(-8, 0)]
        labels2Group = VGroup()
        for l in labels2:
            l.font_size = 36
            labels2Group.add(l)
        
        # real number line
        nl1 = NumberLine(x_range = [-10, 10, 1]).add_numbers()
        
        # point i
        pointi = Dot().move_to([0, 1, 0])
        labeli = Tex("i").move_to([-0.36, 1, 0])
        
        # imaginary axis
        ax = Axes(
            x_length = 20,
            y_length = 20,
            x_range = [-10, 10, 1],
            y_range = [-10, 10, 1],
            y_axis_config = {
                "scaling": ImaginaryBase()
            }
        ).add_coordinates()
        
        # complex plane
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
        
        # example point
        pointEx = Dot().move_to([-3, 2, 0])
        labelEx = Tex("-3+2i").move_to([-3, 1.64, 0])
        
        # animation:
        
        # natural numbers
        self.play(Create(points1Group))
        self.play(Create(labels1Group))
        self.wait(3)
        
        # integers
        self.play(Create(points2Group))
        self.play(Create(labels2Group))
        self.wait(3)
        
        # real numbers
        self.remove(labels1Group)
        self.remove(labels2Group)
        self.add(nl1)
        self.wait(3)
        
        # i
        self.play(Create(pointi))
        self.play(Create(labeli))
        self.wait(3)
        
        # imaginary axis
        self.play(FadeOut(labeli), Create(ax))
        self.play(FadeOut(nl1), FadeOut(pointi), FadeOut(points1Group), FadeOut(points2Group))
        self.wait(3)
        
        # complex plane
        self.bring_to_back(plane1)
        self.play(Create(plane1))
        self.wait(3)
        
        # example point
        self.play(Create(pointEx), Create(labelEx))
        self.wait(3)