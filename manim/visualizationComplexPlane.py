from manim import *

class ComplexPlane(Scene):
    def construct(self):
        points1 = [Dot().move_to([x, 0, 0]) for x in range(0, 8)]
        points1Group = VGroup()
        for p in points1:
            points1Group.add(p)
        labels1 = [Tex(str(x)).move_to([x, -0.36, 0]) for x in range(0, 8)]
        labels1Group = VGroup()
        for l in labels1:
            l.font_size = 36
            labels1Group.add(l)
        
        points2 = [Dot().move_to([x, 0, 0]) for x in range(-8, 0)]
        points2Group = VGroup()
        for p in points2:
            points2Group.add(p)
        labels2 = [Tex(str(x)).move_to([x, -0.36, 0]) for x in range(-8, 0)]
        labels2Group = VGroup()
        for l in labels2:
            l.font_size = 36
            labels2Group.add(l)
        
        pointi = Dot().move_to([0, 1, 0])
        labeli = Tex("i").move_to([-0.36, 1, 0])
        
        nl1 = NumberLine(x_range = [-10, 10, 1]).add_numbers()
        
        pointEx = Dot().move_to([-3, 2, 0])
        labelEx = Tex("-3+2i").move_to([-3, 1.64, 0])
        
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
        
        self.play(Create(points1Group))
        self.play(Create(labels1Group))
        self.wait(3)
        
        self.play(Create(points2Group))
        self.play(Create(labels2Group))
        self.wait(3)
        
        self.remove(labels1Group)
        self.remove(labels2Group)
        self.add(nl1)
        self.wait(3)
        
        self.play(Create(pointi))
        self.play(Create(labeli))
        self.wait(3)
        
        self.play(FadeOut(labeli), Create(ax))
        self.play(FadeOut(nl1), FadeOut(pointi), FadeOut(points1Group), FadeOut(points2Group))
        self.wait(3)
        
        self.bring_to_back(plane1)
        self.play(Create(plane1))
        self.wait(3)
        
        self.play(Create(pointEx), Create(labelEx))
        self.wait(3)

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [("i" if i == 1 else ("-i" if i == -1 else f"{round(i)}i")) for i in val_range]