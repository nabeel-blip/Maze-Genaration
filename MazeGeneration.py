import pygame
from random import randint

import math

screen_size = (800, 800)
number_of_cell_each_row = 20
cell_size = int(screen_size[0] / number_of_cell_each_row)

class Cell:

    def __init__(self, x, y):
        self.visited = False
        self.x = int(x)
        self.y = int(y)
        self.walls = [True, True, True, True]  # top right bottom left
        self.highlight = False

    def set_false(self, wall_number):
        self.walls[wall_number] = False

    def show(self):


        if self.walls[0]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y),
                             actual_coordinates(self.x + 1, self.y), 1)
        if self.walls[1]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x + 1, self.y),
                             actual_coordinates(self.x + 1, self.y + 1), 1)
        if self.walls[2]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y + 1),
                             actual_coordinates(self.x + 1, self.y + 1), 1)
        if self.walls[3]:
            pygame.draw.line(screen, (255, 0, 255), actual_coordinates(self.x, self.y + 1),
                             actual_coordinates(self.x, self.y), 1)
        if self.highlight:
            pygame.draw.rect(screen, (255,255, 0), [self.x * cell_size, self.y * cell_size, cell_size, cell_size])

def actual_coordinates(x, y):
    return x * cell_size, y * cell_size


def show_grid():
    screen.fill((0, 0, 0))
    for i in grid:
        i.show()
    pygame.display.update()




def index(x_coordinate, y_coordinate):
    if x_coordinate < 0 or x_coordinate >= number_of_cell_each_row or y_coordinate < 0 or y_coordinate >= number_of_cell_each_row:
        return None
    temp = x_coordinate + y_coordinate * number_of_cell_each_row

    return int(temp)


def get_neighbours(cur):
    neighbours = []
    try:
        topi = index(cur.x, cur.y - 1)
        top = grid[topi]
        if not top.visited:
            neighbours.append(top)
    except:
        pass

    try:
        righti = index(cur.x + 1, cur.y)
        right = grid[righti]
        if not right.visited:
            neighbours.append(right)
    except:
        pass

    try:
        bottomi = index(cur.x, cur.y + 1)
        bottom = grid[bottomi]
        if not bottom.visited:
            neighbours.append(bottom)
    except:
        pass

    try:
        lefti = index(cur.x - 1, cur.y)
        left = grid[lefti]
        if not left.visited:
            neighbours.append(left)
    except:
        pass

    number_of_unvisited_neighbours = len(neighbours)
    if number_of_unvisited_neighbours > 0:
        '''        
        print("neighbours")
        print(cur.x,cur.y , sep=" ")
        print(number_of_unvisited_neighbours)
        for i in neighbours:
            print(i.x,i.y,end=" | ",sep=",")
        print(" ")
        '''
    if number_of_unvisited_neighbours > 0:
        answer = neighbours[randint(0, number_of_unvisited_neighbours - 1)]
     #  print("returning",answer.x,answer.y)
        return answer

    return None


def remove_walls(current_cell, next_cell):
    temp = current_cell.x - next_cell.x
    if temp > 0:
        current_cell.set_false(3)  # left
        next_cell.set_false(1)  # right
        return

    elif temp < 0:
        current_cell.set_false(1)  # right
        next_cell.set_false(3)  # left
        return

    temp = current_cell.y - next_cell.y
    if temp > 0:
        current_cell.set_false(0)  # up
        next_cell.set_false(2)  # down
        return

    elif temp < 0:
        current_cell.set_false(2)
        next_cell.set_false(0)


pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Maze Generation")
run = True
grid = []
for x in range(0, number_of_cell_each_row):
    for y in range(0, number_of_cell_each_row):
        grid.append(Cell(y, x))

stack = []
current = grid[0]

current.visited = True
count = 0
while True:
    count+=1
    print(count)
    current.highlight = True
    show_grid()
    # print(current.x, current.y)
    next = get_neighbours(current)
    if not next:
        print("done")
        current.highlight = False
        current = stack.pop()
    else:
        next.visited = True
        remove_walls(current, next)
        stack.append(current)
        current.highlight = False
        current = next

    if len(stack) <= 0:
        break

print("one")
show_grid()
while run:

    # pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
