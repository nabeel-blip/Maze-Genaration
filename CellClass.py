import pygame
from HelperFunctions import actual_coordinates



class Cell:

    def __init__(self, x, y):
        self.visited = False
        self.x = int(x)
        self.y = int(y)
        self.walls = [True, True, True, True]  # top right bottom left
        self.highlight = False
        self.stacked = False;

    def print_coordinates(self):
        print(self.x, self.y)

    def set_false(self, wall_number):
        self.walls[wall_number] = False

    def show(self, screen, cell_size, con = True):

        if self.walls[0]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y, cell_size),
                             actual_coordinates(self.x + 1, self.y, cell_size), 1)
        if self.walls[1]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x + 1, self.y, cell_size),
                             actual_coordinates(self.x + 1, self.y + 1, cell_size), 1)
        if self.walls[2]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y + 1, cell_size),
                             actual_coordinates(self.x + 1, self.y + 1, cell_size), 1)
        if self.walls[3]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y + 1, cell_size),
                             actual_coordinates(self.x, self.y, cell_size), 1)
        if self.highlight and con:
            pygame.draw.rect(screen, (255, 0, 255),
                             [self.x * cell_size + cell_size / 4, self.y * cell_size + cell_size / 4,
                              cell_size / 2,
                              cell_size / 2])
