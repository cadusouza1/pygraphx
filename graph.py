import pygame


class Function:
    def __init__(
        self, name: str, color: pygame.Color, points: list[tuple[float, float]]
    ) -> None:
        self.name = name
        self.color = color
        self.points = points


class Graph:
    def __init__(self):
        self.functions: list[Function] = []

    def add_function(
        self,
        name: str,
        f,
        frange: tuple[int, int],
        color: pygame.Color = pygame.Color(255, 0, 0),
    ):
        self.functions.append(
            Function(
                name,
                color,
                [(x, f(x)) for x in range(frange[0], frange[1])],
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
                    surface.get_width() / 2 + point[0],
                    surface.get_height() / 2 - point[1],
                ),
                points,
            )
        )
