from manim import *

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
        
        self.play(Create(plane1), Create(ax))
        self.wait(1)

class ImaginaryBase(LinearBase):
    def __init__(self, scale_factor: float = 1, custom_labels: bool = True):
        super().__init__(scale_factor)
        self.custom_labels = custom_labels
    def get_custom_labels(self, val_range):
        return [f"{round(i)}i" for i in val_range]