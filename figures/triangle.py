from figures.figure import Figure
import numpy as np

class Triangle(Figure):
    def __init__(self, c1: tuple, c2: tuple, c3: tuple):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def tobytes(self) -> bytes:
        arr = np.array([
            *self.c1,
            *self.c2,
            *self.c3
        ], dtype=np.float32)

        return arr.tobytes()
