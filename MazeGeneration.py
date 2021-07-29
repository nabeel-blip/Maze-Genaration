import pygame
from random import randint
from CellClass  import Cell

screen_size = (800, 800)
number_of_cell_each_row = 40
cell_size = int(screen_size[0] / number_of_cell_each_row)
margin = 5


def show_grid():
    screen.fill((0, 0, 0))
    for i in grid:
        i.show(screen,cell_size)
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

while True:
    pygame.event.get()

    current.highlight = True
    show_grid()

    next = get_neighbours(current)
    if not next:

        current.highlight = False
        current = stack.pop()
        current.stacked = False
    else:
        next.visited = True
        remove_walls(current, next)
        current.stacked = True
        current.highlight = False
        stack.append(current)
        current = next

    if len(stack) <= 0:
        break

print("done")
show_grid()
while run:

    # pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
