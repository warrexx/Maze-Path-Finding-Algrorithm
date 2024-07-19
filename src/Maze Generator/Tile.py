import pygame
from random import choice


class Tile:

    def __init__(self, x: int, y: int, TILE: int, screen: pygame.surface) -> None:
        self.Tile = TILE
        self.x = x
        self.y = y
        self.screen = screen
        self.visited = False
        self.walls = {
            "top": True,
            "bottom": True,
            "left": True,
            "right": True,
        }

    def draw(self):
        TILE = self.Tile
        coordinat_x = self.x * TILE
        coordinat_y = self.y * TILE

        pygame.draw.rect(
            self.screen,
            "red",
            (coordinat_x, coordinat_y, TILE, TILE),
        )

    def draw_tile(self):
        thickness = 2
        TILE = self.Tile
        coordinat_x = self.x * TILE
        coordinat_y = self.y * TILE

        if self.visited:
            pygame.draw.rect(
                self.screen, "black", (coordinat_x, coordinat_y, TILE, TILE)
            )

        # walls
        walls = self.walls
        if walls["top"]:
            pygame.draw.line(
                self.screen,
                "orange",
                (coordinat_x, coordinat_y),
                (coordinat_x + TILE, coordinat_y),
                width=thickness,
            )

        if walls["bottom"]:
            pygame.draw.line(
                self.screen,
                "orange",
                (coordinat_x, coordinat_y + TILE),
                (coordinat_x + TILE, coordinat_y + TILE),
                width=thickness,
            )

        if walls["left"]:
            pygame.draw.line(
                self.screen,
                "orange",
                (coordinat_x, coordinat_y),
                (coordinat_x, coordinat_y + TILE),
                width=thickness,
            )

        if walls["top"]:
            pygame.draw.line(
                self.screen,
                "orange",
                (coordinat_x + TILE, coordinat_y),
                (coordinat_x + TILE, coordinat_y + TILE),
                width=thickness,
            )

    def check_neighbours(self, maze):
        x, y = self.x, self.y

        neighbours = []

        total_rows = len(maze)
        total_cols = len(maze[0])

        if not x <= 0:
            left = maze[x - 1][y]
            if not left.visited:
                neighbours.append(left)

        if not x > total_rows:
            right = maze[x + 1][y]
            if not right.visited:
                neighbours.append(right)

        if not y <= 0:
            top = maze[x][y - 1]
            if not top.visited:
                neighbours.append(top)

        if not y > total_cols:
            bottom = maze[x][y + 1]
            if not bottom.visited:
                neighbours.append(bottom)

        return neighbours

    def move(self, maze: list[list["Tile"]]):
        neighbours = self.check_neighbours(maze)

        if neighbours:
            return choice(neighbours)

        return False

    @staticmethod
    def remove_wall(current_tile: "Tile", next_tile: "Tile"):
        dx = next_tile.x - current_tile.x
        dy = next_tile.y - current_tile.y

        if dx == 1:
            current_tile.walls["right"] = False
            next_tile.walls["left"] = False

        elif dx == -1:
            current_tile.walls["left"] = False
            next_tile.walls["right"] = False

        if dy == 1:
            current_tile.walls["bottom"] = False
            next_tile.walls["top"] = False

        elif dy == -1:
            current_tile.walls["top"] = False
            next_tile.walls["bottom"] = False
