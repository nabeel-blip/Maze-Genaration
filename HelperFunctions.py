import pygame
from random import randint


def show_grid(screen, grid, cell_size):
    screen.fill((0, 0, 0))
    for i in grid:
        i.show(screen, cell_size)
    pygame.display.update()


def index(x_coordinate, y_coordinate, number_of_cell_each_row):
    if x_coordinate < 0 or x_coordinate >= number_of_cell_each_row or y_coordinate < 0 or y_coordinate >= number_of_cell_each_row:
        return None
    temp = x_coordinate + y_coordinate * number_of_cell_each_row

    return int(temp)


def get_neighbours(cur, grid, number_of_cell_each_row):
    neighbours = []
    try:
        topi = index(cur.x, cur.y - 1, number_of_cell_each_row)
        top = grid[topi]
        if not top.visited:
            neighbours.append(top)
    except:
        pass

    try:
        righti = index(cur.x + 1, cur.y, number_of_cell_each_row)
        right = grid[righti]
        if not right.visited:
            neighbours.append(right)
    except:
        pass

    try:
        bottomi = index(cur.x, cur.y + 1, number_of_cell_each_row)
        bottom = grid[bottomi]
        if not bottom.visited:
            neighbours.append(bottom)
    except:
        pass

    try:
        lefti = index(cur.x - 1, cur.y, number_of_cell_each_row)
        left = grid[lefti]
        if not left.visited:
            neighbours.append(left)
    except:
        pass

    return neighbours


def get_random_neighbour(neighbours):
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
