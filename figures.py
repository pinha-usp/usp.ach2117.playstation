from typing import List, Tuple
import numpy as np
import moderngl

class Figure:

    def __init__(
        self,
        coordinates: List[Tuple[float, float]], # List of (x, y) coordinates
        color: Tuple[float, float, float], # (r, g, b) color 
        mode: int
    ):
        self.coordinates = coordinates
        self.color = color
        self.mode = mode

    def to_array(self) -> np.ndarray:
        coordinates = np.array(self.coordinates, dtype=np.float32)

        color = np.array(self.color, dtype=np.float32)

        colors = np.tile(color, (len(self.coordinates), 1))

        return np.hstack((coordinates, colors))

    def translate(self, dx: float, dy: float):
        self.coordinates = [
            (x + dx, y + dy)
            for x,y
            in self.coordinates
        ]

        return self

    def rotate(self, angle: float):
        self.coordinates = [
            (
                x * np.cos(angle) - y * np.sin(angle),
                x * np.sin(angle) + y * np.cos(angle)
            )
            for x, y
            in self.coordinates
        ]

        return self

class Triangle(Figure):

    def __init__(
        self,
        c1: Tuple[float, float],
        c2: Tuple[float, float],
        c3: Tuple[float, float],
        color: Tuple[float, float, float]
    ):
        super().__init__(
            coordinates=[c1, c2, c3],
            color=color,
            mode=moderngl.TRIANGLES
        )

class EquilateralTriangle(Triangle):

    def __init__(
        self,
        center: Tuple[float, float],
        side: float,
        color: Tuple[float, float, float]
    ):
        c1 = (
            center[0] - side / 2,
            center[1] - np.sqrt(3) * side / 6
        )

        c2 = (
            center[0] + side / 2,
            center[1] - np.sqrt(3) * side / 6
        )

        c3 = (
            center[0],
            center[1] + np.sqrt(3) * side / 3
        )

        super().__init__(
            c1 = c1,
            c2 = c2,
            c3 = c3,
            color = color
        )

class Rectangle(Figure):

    def __init__(
        self,
        center: Tuple[float, float],
        width: float,
        height: float,
        color: Tuple[float, float, float]
    ):
        c1 = (
            center[0] - width / 2,
            center[1] - height / 2
        )

        c2 = (
            center[0] + width / 2,
            center[1] - height / 2
        )

        c3 = (
            center[0] + width / 2,
            center[1] + height / 2
        )

        c4 = (
            center[0] - width / 2,
            center[1] + height / 2
        )

        super().__init__(
            coordinates=[c1, c2, c3, c4],
            color=color,
            mode=moderngl.TRIANGLE_FAN
        )

class Circle(Figure):
    
        def __init__(
            self,
            center: Tuple[float, float],
            radius: float,
            color: Tuple[float, float, float],
            n_points: int = 100
        ):
            coordinates = [
                (
                    center[0] + radius * np.cos(angle),
                    center[1] + radius * np.sin(angle)
                )
                for angle
                in np.linspace(0, 2 * np.pi, n_points)
            ]
    
            super().__init__(
                coordinates=coordinates,
                color=color,
                mode=moderngl.TRIANGLE_FAN
            )

button_color = (0.0, 0.0, 0.0)

square_color = (0.831, 0.56, 0.73)
triangle_color = (0.211, 0.866, 0.796)
circle_color = (0.921, 0.439, 0.407)
x_color = (0.607, 0.674, 0.901)

window_figures: List[Figure] = [
    # Botão quadrado
    Circle(
        center = (-0.6, 0.0),
        radius = 0.35,
        color = button_color
    ),

    Rectangle(
        center = (-0.6, 0.0),
        width = 0.4,
        height = 0.4,
        color = square_color 
    ),

    Rectangle(
        center = (-0.6, 0.0),
        width = 0.3,
        height = 0.3,
        color = button_color
    ),

    # Botão triângulo
    Circle(
        center = (0.0, 0.6),
        radius = 0.35,
        color = button_color 
    ),

    EquilateralTriangle(
        center = (0.0, 0.6),
        side = 0.5,
        color = triangle_color
    ),

    EquilateralTriangle(
        center = (0.0, 0.6),
        side = 0.3,
        color = button_color 
    ),

    # Botão círculo
    Circle(
        center = (0.6, 0.0),
        radius = 0.35,
        color = button_color
    ),

    Circle(
        center = (0.6, 0.0),
        radius = 0.25,
        color = circle_color 
    ),

    Circle(
        center = (0.6, 0.0),
        radius = 0.20,
        color = button_color
    ),

    # Botão x
    Circle(
        center = (0.0, -0.6),
        radius = 0.35,
        color = button_color 
    ),

    Rectangle(
        center = (0.0, -0.6),
        width = 0.08,
        height = 0.5,
        color = x_color
    ).translate(0.0, 0.6).rotate(np.radians(45)).translate(0.0, -0.6),

    Rectangle(
        center = (0.0, -0.6),
        width = 0.5,
        height = 0.08,
        color = x_color
    ).translate(0.0, 0.6).rotate(np.radians(225)).translate(0.0, -0.6),
]
