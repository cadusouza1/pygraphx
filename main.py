import pygame


def f(x: float) -> float:
    return x**2


pygame.init()

screen = pygame.display.set_mode((1280, 720))
graph_x_offset = 50
graph_y_offset = 50
graph = pygame.Surface(
    (screen.get_width() - graph_x_offset, screen.get_height() - graph_y_offset)
)

points = [(x, f(x)) for x in range(-graph.get_width(), graph.get_width())]
points_color = pygame.Color(255, 0, 0)

translated_points = list(
    map(
        lambda point: (
            graph.get_width() / 2 + point[0],
            graph.get_height() / 2 - point[1],
        ),
        points,
    )
)

arrow_sidelength = 20
arrow_height = arrow_sidelength * (3**0.5) / 2

axis_color = pygame.Color(255, 0, 255)

x_axis_up_arrow = (
    (graph.get_width() / 2, 0),
    (
        graph.get_width() / 2 - arrow_sidelength / 2,
        arrow_height,
    ),
    (
        graph.get_width() / 2 + arrow_sidelength / 2,
        arrow_height,
    ),
)

x_axis_down_arrow = (
    (graph.get_width() / 2, graph.get_height()),
    (
        graph.get_width() / 2 + arrow_sidelength / 2,
        graph.get_height() - arrow_height,
    ),
    (
        graph.get_width() / 2 - arrow_sidelength / 2,
        graph.get_height() - arrow_height,
    ),
)

y_axis_left_arrow = (
    (0, graph.get_height() / 2),
    (
        arrow_height,
        graph.get_height() / 2 - arrow_sidelength / 2,
    ),
    (
        arrow_height,
        graph.get_height() / 2 + arrow_sidelength / 2,
    ),
)

y_axis_right_arrow = (
    (graph.get_width(), graph.get_height() / 2),
    (
        graph.get_width() - arrow_height,
        graph.get_height() / 2 - arrow_sidelength / 2,
    ),
    (
        graph.get_width() - arrow_height,
        graph.get_height() / 2 + arrow_sidelength / 2,
    ),
)

x_axis_coords = (
    (graph.get_width() / 2, 0),
    (graph.get_width() / 2, graph.get_height()),
)

y_axis_coords = (
    (0, graph.get_height() / 2),
    (graph.get_width(), graph.get_height() / 2),
)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.lines(graph, axis_color, True, x_axis_coords)
    pygame.draw.lines(graph, axis_color, True, y_axis_coords)
    pygame.draw.lines(graph, points_color, True, translated_points)
    pygame.draw.polygon(graph, axis_color, x_axis_up_arrow)
    pygame.draw.polygon(graph, axis_color, x_axis_down_arrow)
    pygame.draw.polygon(graph, axis_color, y_axis_left_arrow)
    pygame.draw.polygon(graph, axis_color, y_axis_right_arrow)

    screen.blit(graph, (graph_x_offset / 2, graph_y_offset / 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
