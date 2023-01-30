from manim import *
from colorThemes import *
from axisLabels import *

class Title(Scene):
    def construct(self):
        title = Tex("Mandelbrot")
        title.font_size = 80
        self.play(Create(title))
        self.wait(3)
        self.play(FadeOut(title, shift = UP))

class Mandelbrot(MovingCameraScene):
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
                "scaling": ImaginaryBase(scale_factor = 1, custom_labels = True)
            }
        ).add_coordinates()
        
        # example points
        pc = Dot().move_to([1, 0.5, 0])
        pz = Dot().move_to([0, 0, 0]).set_color(self.COLORS["highlight"])
        lc = Tex("c").move_to([1.2, 0.3, 0]).add_updater(lambda x: x.move_to([pc.get_x() + 0.2, pc.get_y() - 0.2, 0]))
        lz = Tex("z").move_to([0.2, -0.2, 0]).set_color(self.COLORS["highlight"])
        
        # iteration tracker
        pzSteps = VGroup()
        pzSteps.add(Dot(radius = 0.04).move_to([0, 0, 0]).set_color(self.COLORS["highlight"]))
        def getStep(n):
            return Dot(radius = 0.04).set_color(self.COLORS["highlight"]).add_updater(lambda x: x.move_to([
                pzSteps[n].get_x() * pzSteps[n].get_x() - pzSteps[n].get_y() * pzSteps[n].get_y() + pc.get_x(),
                2 * pzSteps[n].get_x() * pzSteps[n].get_y() + pc.get_y(),
                0
            ] if (abs(pzSteps[n].get_x()) < 50 and abs(pzSteps[n].get_y()) < 50) else [
                pzSteps[n].get_x(),
                pzSteps[n].get_y(),
                0
            ]))
        
        for i in range(0, 20):
            pzSteps.add(getStep(i))
        
        # animation paths
        path1 = CubicBezier([1, 0.5, 0], [0, -4, 0], [-4, 0, 0], [0, 1.5, 0])
        path2 = CubicBezier([0, 1.5, 0], [1, 1, 0], [-2.5, 0, 0], [1, -0.5, 0])
        
        # divergence border (circle)
        circle = Circle(radius = 2).set_color(self.COLORS["highlight"])
        
        # mandelbrot images
        image1 = ImageMobject("resources/mandelbrot.jpeg")
        image1.height = 4
        image2 = ImageMobject("resources/frame1.png")
        image2.height = 4
        image3 = ImageMobject("resources/frame2.png")
        image3.height = 4
        image4 = ImageMobject("resources/frame_^2.png")
        image4.height = 4
        image5 = ImageMobject("resources/frame_^3.png")
        image5.height = 4
        image6 = ImageMobject("resources/frame_^4.png")
        image6.height = 4
        image7 = ImageMobject("resources/frame_^2mal-1.7+^3.png")
        image7.height = 4
        image8 = ImageMobject("resources/frame_burningship.png")
        image8.height = 4
        
        # animation:
        
        # create complex plane
        self.play(Create(plane1), Create(ax))
        self.wait(1)
        
        # create example points
        self.play(Create(pc), Create(lc))
        self.play(Create(pz), Create(lz))
        self.wait(1)
        
        # do some iterations
        self.play(pz.animate.move_to([1, 0.5, 0]), lz.animate.move_to([1.2, 0.3, 0]))
        self.wait(1)
        self.play(pz.animate.move_to([1.75, 1.5, 0]), lz.animate.move_to([1.95, 1.3, 0]))
        self.wait(1)
        self.play(pz.animate.move_to([1.8125, 5.75, 0]), lz.animate.move_to([2.0125, 5.55, 0]))
        self.remove(pz, lz)
        self.wait(1)
        
        # add iteration tracker
        self.play(FadeIn(pzSteps))
        self.wait(1)
        
        # move c around
        self.play(MoveAlongPath(pc, path1, run_time = 3, rate_func = linear))
        self.wait(1)
        
        # show circle
        self.play(FadeIn(circle))
        self.wait(1)
        
        # zoom in
        self.play(self.camera.frame.animate.set(height = 4))
        self.wait(1)
        
        # move c around again
        self.play(MoveAlongPath(pc, path2, run_time = 10, rate_func = linear))
        self.wait(1)
        
        # remove example points and add images
        self.play(FadeOut(pc), FadeOut(lc), FadeOut(pzSteps), FadeOut(circle))
        self.play(FadeIn(image1))
        self.wait(1)
        self.play(FadeIn(image2))
        self.play(FadeOut(image1))
        self.wait(1)
        self.play(FadeIn(image3))
        self.remove(image2)
        self.wait(1)
        self.play(FadeIn(image4))
        self.remove(image3)
        self.wait(1)
        self.play(FadeIn(image5))
        self.remove(image4)
        self.wait(1)
        self.play(FadeIn(image6))
        self.remove(image5)
        self.wait(1)
        self.play(FadeIn(image7))
        self.remove(image6)
        self.wait(1)
        self.play(FadeIn(image8))
        self.remove(image7)
        self.wait(1)
        
        # remove objects
        self.play(FadeOut(image8))
        self.wait(1)
        self.play(FadeOut(plane1), FadeOut(ax))