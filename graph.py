from typing import Any, Callable, Generator

import pygame

MAX_NUM_OF_POINTS = 100_000


class Function:
    def __init__(
        self,
        name: str,
        f: Callable[[float], float],
        color: pygame.Color,
        points: list[tuple[float, float]],
    ) -> None:
        self.name = name
        self.color = color
        self.points = points
        self.f = f


class Graph:
    def __init__(self):
        self.functions: list[Function] = []
        self.scale: float = 1

    def add_function(
        self,
        name: str,
        f: Callable[[float], float],
        xrange_start: int,
        xrange_end: int,
        color: pygame.Color = pygame.Color(255, 0, 0),
    ):
        self.functions.append(
            Function(
                name,
                f,
                color,
                [(x, f(x)) for x in range(xrange_start, xrange_end)],
            )
        )

    def blit_functions(self, surface: pygame.Surface):
        for function in self.functions:
            pygame.draw.lines(
                surface,
                function.color,
                True,
                self.translate_points(function.points, surface),
            )

    def translate_points(
        self, points: list[tuple[float, float]], surface: pygame.Surface
    ) -> list[tuple[float, float]]:
        return list(
            map(
                lambda point: (
                    surface.get_width() / 2 + point[0] * self.scale,
                    surface.get_height() / 2 - point[1] * self.scale,
                ),
                points,
            )
        )

    def _generate_points(
        self, start: float, end: float, step: float
    ) -> Generator[float, Any, None]:
        max_step = (end - start) / MAX_NUM_OF_POINTS
        step = max(max_step, step)

        while start <= end:
            yield start
            start += step

    def update_function_points(self):
        for i, function in enumerate(self.functions):
            self.functions[i].points = list(
                map(
                    lambda x: (x, function.f(x)),
                    self._generate_points(
                        function.points[0][0],
                        function.points[-1][0],
                        1 / self.scale,
                    ),
                )
            )
