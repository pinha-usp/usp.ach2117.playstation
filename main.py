import moderngl_window as mglw
import pathlib
from figures.triangle import Triangle

class Figures(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "2D Figures"
    resource_dir = pathlib.Path("resources")
    fullscreen = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.program = self.load_program(
            vertex_shader="shaders/vertex.glsl",
            fragment_shader="shaders/fragment.glsl",
        )

        triangle = Triangle(
            (0.0, 1.0, 0.0),
            (-1.0, -1.0, 0.0),
            (1.0, -1.0, 0.0)
        )

        triangle_buffer = self.ctx.buffer(triangle.tobytes())

        self.vao = self.ctx.vertex_array(self.program, triangle_buffer, "position")

    def render(self, time, frametime):
        self.ctx.clear()
        self.vao.render()

Figures.run()
