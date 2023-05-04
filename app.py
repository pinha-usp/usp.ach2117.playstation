import pathlib
import moderngl_window as mglw
from figures.triangle import Triangle 

class App(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "2D Figures"
    resource_dir = pathlib.Path("resources")
    fullscreen = True
    aspect_ratio = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.triangle = Triangle(
            app=self,
            c1=(-0.5, -0.5),
            c2=(0.0, 0.5),
            c3=(0.5, -0.5)
        )

    def render(self, time, frametime):
        self.ctx.clear()
        self.triangle.render()

App.run()
