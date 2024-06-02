import pygame
from random import choice


class Mouse:
    def __init__(self, x, y, screen, color, TILE=15) -> None:
        self.x = x
        self.y = y
        self.screen = screen
        self.visited = False
        self.color = color
        self.TILE = TILE
        self.previous_tile: Mouse = None
        self.g_cost = 0
        self.h_cost = 1000
        self.f_cost = 0
        self.explored = False

    def draw(self):
        TILE = self.TILE
        screen = self.screen
        radius = 5

        coordinat_x = self.x * TILE
        coordinat_y = self.y * TILE

        pygame.draw.circle(
            screen,
            "blue",
            (coordinat_x + TILE / 2, coordinat_y + TILE / 2),
            radius,
        )

    def draw_pos(self):
        TILE = self.TILE
        coordinat_x = self.x * TILE
        coordinat_y = self.y * TILE
        screen = self.screen
        radius = 5
        # color = self.color

        if self.visited:
            pygame.draw.circle(
                screen,
                "orange",
                (coordinat_x + TILE / 2, coordinat_y + TILE / 2),
                radius,
            )

        if self.explored:
            pygame.draw.circle(
                screen,
                "gray",
                (coordinat_x + TILE / 2, coordinat_y + TILE / 2),
                radius,
            )

    def draw_path(self):
        screen = self.screen
        TILE = self.TILE

        x = self.x * TILE
        y = self.y * TILE

        color = self.color
        radius = 5

        pygame.draw.circle(
            screen,
            color,
            (x + TILE / 2, y + TILE / 2),
            radius,
        )

    def check_next_tile_candidates(self, mouse_pos, maze):

        rows = len(mouse_pos)
        cols = len(mouse_pos[0])

        x = self.x
        y = self.y

        next_tile_candidates = []

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if abs(dx) == abs(dy):
                    continue

                if dx == 0 and dy == -1:
                    current_wall, next_wall = "top", "bottom"

                elif dx == 0 and dy == 1:
                    current_wall, next_wall = "bottom", "top"

                elif dx == -1 and dy == 0:
                    current_wall, next_wall = "left", "right"

                elif dx == 1 and dy == 0:
                    current_wall, next_wall = "right", "left"

                next_x = x + dx
                next_y = y + dy

                if not (0 <= next_x < rows) or not (0 <= next_y < cols):
                    continue

                next_pos = mouse_pos[next_x][next_y]
                next_tile = maze[next_x][next_y]
                current_tile = maze[x][y]

                if (
                    not next_pos
                    and not next_tile.walls[next_wall]
                    and not current_tile.walls[current_wall]
                ):
                    next_tile_candidates.append(next_pos)

        if next_tile_candidates:
            return next_tile_candidates

        return False
