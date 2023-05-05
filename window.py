import pathlib
from typing import List
import numpy as np
import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO
from figures import window_figures

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "2D Figures"
    resource_dir = pathlib.Path("resources")
    aspect_ratio = 1.0
    fullscreen = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.figures = window_figures
        self.__init_vaos()
        self.__init_program()

    def __init_vaos(self):
        self.vaos = []

        for figure in self.figures:
            vao = VAO(mode = figure.mode)

            vao.buffer(
                buffer = figure.to_array(),
                buffer_format = "2f 3f",
                attribute_names = ["in_position", "in_color"]
            )

            self.vaos.append(vao)

    def __init_program(self):
        name = "default"

        self.program = self.load_program(
            vertex_shader = f"shaders/{name}.vert",
            fragment_shader = f"shaders/{name}.frag"
        )

    def render(self, time, frametime):
        self.ctx.clear(1.0, 1.0, 0.992)

        for vao in self.vaos:
            vao.render(self.program)

Window.run()
