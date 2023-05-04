import moderngl
from figures.figure import Figure

class Triangle(Figure):
    def __init__(self, app, c1: tuple, c2: tuple, c3: tuple):
        super().__init__(
            app=app,
            coordinates=[c1, c2, c3],
            mode=moderngl.TRIANGLE_STRIP,
            color=(1.0, 0.0, 0.0)
        )
