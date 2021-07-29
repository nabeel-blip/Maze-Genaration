import pygame


class Cell:

    def __init__(self, x, y):
        self.visited = False
        self.x = int(x)
        self.y = int(y)
        self.walls = [True, True, True, True]  # top right bottom left
        self.highlight = False
        self.stacked = False;

    def set_false(self, wall_number):
        self.walls[wall_number] = False

    def actual_coordinates(self, x, y, cell_size):
        return x * cell_size, y * cell_size

    def show(self, screen, cell_size):

        if self.walls[0]:
            pygame.draw.line(screen, (255, 0, 255), self.actual_coordinates(self.x, self.y, cell_size),
                             self.actual_coordinates(self.x + 1, self.y, cell_size), 1)
        if self.walls[1]:
            pygame.draw.line(screen, (255, 0, 255), self.actual_coordinates(self.x + 1, self.y, cell_size),
                             self.actual_coordinates(self.x + 1, self.y + 1, cell_size), 1)
        if self.walls[2]:
            pygame.draw.line(screen, (255, 0, 255), self.actual_coordinates(self.x, self.y + 1, cell_size),
                             self.actual_coordinates(self.x + 1, self.y + 1, cell_size), 1)
        if self.walls[3]:
            pygame.draw.line(screen, (255, 0, 255), self.actual_coordinates(self.x, self.y + 1, cell_size),
                             self.actual_coordinates(self.x, self.y, cell_size), 1)
        if self.highlight:
            pygame.draw.rect(screen, (255, 255, 0), [self.x * cell_size, self.y * cell_size, cell_size, cell_size])
