import itertools
import numpy as np

class Figure:

    vert_shader = "default"
    frag_shader = "default"

    def __init__(self, app, mode, coordinates, color):
        self.coordinates = coordinates
        self.color = color
        self.mode = mode
        self.app = app
        self.program = self.__create_program()
        self.vbo = self.__create_vbo()
        self.vao = self.__create_vao()

    def __create_program(self):
        vert_path = f"shaders/{self.vert_shader}.vert"
        frag_path = f"shaders/{self.frag_shader}.frag"

        return self.app.load_program(
            vertex_shader=vert_path,
            fragment_shader=frag_path
        )

    def __create_vbo(self):
        return self.app.ctx.buffer(self.__tobytes())

    def __create_vao(self):
        return self.app.ctx.simple_vertex_array(
            self.program,
            self.vbo,
            "in_position"
        )

    def __tobytes(self) -> bytes:
        coordinates = list(itertools.chain.from_iterable(self.coordinates))

        return np.array(coordinates, dtype=np.float32).tobytes()

    def render(self):
        self.vao.render(self.mode)
