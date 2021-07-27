
import pygame
import math
screen_size = (800, 800)
number_of_cell_each_row=80
cell_size = screen_size[0]/number_of_cell_each_row
center_screen = (screen_size[0]/2, screen_size[1]/2)

class Cell:

    def __init__(self, x, y):
        self.x = x * cell_size
        self.y = y * cell_size
        self.walls = [True, True, True, True]  # top right bottom left

    def show(self):
        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x+cell_size, self.y), 1)
        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255), (self.x+cell_size, self.y), (self.x+cell_size, self.y+cell_size), 1)
        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255), (self.x+cell_size, self.y+cell_size), (self.x, self.y+cell_size), 1)
        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255), (self.x, self.y+cell_size), (self.x, self.y), 1)

def show_grid():
    for i in grid:
        i.show()
    pygame.display.update()
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Maze Generation")
run = True
grid = []
for x in range(0,number_of_cell_each_row):
    for y in range(0,number_of_cell_each_row):
        grid.append(Cell(x, y))

show_grid()
while run:
    screen.fill((0, 0, 0))
   # pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

