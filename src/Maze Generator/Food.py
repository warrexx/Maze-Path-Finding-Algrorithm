import pygame


class Food:
    def __init__(self, x, y, screen: pygame.surface, TILE) -> None:
        self.x = x
        self.y = y
        self.screen = screen
        self.TILE = TILE

    def draw(self):
        TILE = self.TILE
        screen = self.screen
        radius = 5  # pixel

        pygame.draw.circle(screen, "red", (self.x + TILE + TILE / 2), radius)
