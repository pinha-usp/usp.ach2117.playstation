import moderngl_window as mglw
import pathlib
import numpy as np

class Figures(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "2D Figures"
    fullscreen = True
    resource_dir = pathlib.Path("resources")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.program = self.load_program(
            vertex_shader="shaders/vertex.glsl",
            fragment_shader="shaders/fragment.glsl",
        )

        triangle = np.array([
            0.0, 0.5, 0.0,
            -0.5, -0.5, 0.0,
            0.5, -0.5, 0.0
        ], dtype=np.float32)

        triangle_buffer = self.ctx.buffer(triangle.tobytes())

        self.vao = self.ctx.vertex_array(self.program, triangle_buffer, "position")

    def render(self, time, frametime):
        self.ctx.clear()
        self.vao.render()

Figures.run()
