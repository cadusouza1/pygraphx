import pygame

import graph

pygame.init()

screen = pygame.display.set_mode((1280, 720))
graph_x_offset = 50
graph_y_offset = 50
graph_surface = pygame.Surface(
    (screen.get_width() - graph_x_offset, screen.get_height() - graph_y_offset)
)

function_graph = graph.Graph()
function_graph.add_function(
    "x^2",
    lambda x: x**2,
    (-graph_surface.get_width(), graph_surface.get_width()),
    pygame.Color(255, 255, 0),
)

function_graph.add_function(
    "x",
    lambda x: x,
    (-graph_surface.get_width(), graph_surface.get_width()),
    pygame.Color(0, 255, 0),
)

arrow_sidelength = 10
arrow_height = arrow_sidelength * (3**0.5) / 2

axis_color = pygame.Color(255, 255, 255)

x_axis_up_arrow = (
    (graph_surface.get_width() / 2, 0),
    (
        graph_surface.get_width() / 2 - arrow_sidelength / 2,
        arrow_height,
    ),
    (
        graph_surface.get_width() / 2 + arrow_sidelength / 2,
        arrow_height,
    ),
)

x_axis_down_arrow = (
    (graph_surface.get_width() / 2, graph_surface.get_height()),
    (
        graph_surface.get_width() / 2 + arrow_sidelength / 2,
        graph_surface.get_height() - arrow_height,
    ),
    (
        graph_surface.get_width() / 2 - arrow_sidelength / 2,
        graph_surface.get_height() - arrow_height,
    ),
)

y_axis_left_arrow = (
    (0, graph_surface.get_height() / 2),
    (
        arrow_height,
        graph_surface.get_height() / 2 - arrow_sidelength / 2,
    ),
    (
        arrow_height,
        graph_surface.get_height() / 2 + arrow_sidelength / 2,
    ),
)

y_axis_right_arrow = (
    (graph_surface.get_width(), graph_surface.get_height() / 2),
    (
        graph_surface.get_width() - arrow_height,
        graph_surface.get_height() / 2 - arrow_sidelength / 2,
    ),
    (
        graph_surface.get_width() - arrow_height,
        graph_surface.get_height() / 2 + arrow_sidelength / 2,
    ),
)

x_axis_coords = (
    (graph_surface.get_width() / 2, 0),
    (graph_surface.get_width() / 2, graph_surface.get_height()),
)

y_axis_coords = (
    (0, graph_surface.get_height() / 2),
    (graph_surface.get_width(), graph_surface.get_height() / 2),
)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.lines(graph_surface, axis_color, True, x_axis_coords)
    pygame.draw.lines(graph_surface, axis_color, True, y_axis_coords)
    function_graph.blit_functions(graph_surface)
    # pygame.draw.lines(graph_surface, points_color, True, translated_points)
    pygame.draw.polygon(graph_surface, axis_color, x_axis_up_arrow)
    pygame.draw.polygon(graph_surface, axis_color, x_axis_down_arrow)
    pygame.draw.polygon(graph_surface, axis_color, y_axis_left_arrow)
    pygame.draw.polygon(graph_surface, axis_color, y_axis_right_arrow)

    screen.blit(graph_surface, (graph_x_offset / 2, graph_y_offset / 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
