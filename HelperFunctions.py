import pygame
from random import randint


def actual_coordinates(x, y, cell_size):
    return x * cell_size, y * cell_size


def show_grid(screen, grid, cell_size, con = True):
    screen.fill((0, 0, 0))
    for i in grid:
        i.show(screen, cell_size,con)
    pygame.display.update()


def print_path(path, screen, cell_size):
    for x in path:
        x.show(screen, cell_size, (255, 0, 1))
        pygame.display.update()


def print_path2(path, screen, cell_size):
    for x in range(0, len(path)):
        try:
            if not (path[x].x - path[x + 1].x):
                pygame.draw.line(screen, (255, 0, 255), actual_coordinates(path[x].x + 0.5, path[x].y + 0.2, cell_size),
                                 actual_coordinates(path[x].x + .5, path[x].y + .8, cell_size), 1)
            else:
                pygame.draw.line(screen, (255, 0, 255), actual_coordinates(path[x].x + 0.2, path[x].y + 0.5, cell_size),
                                 actual_coordinates(path[x].x + .8, path[x].y + .5, cell_size), 1)
        except:
            pygame.draw.rect(screen, (255, 0, 255),
                             [path[x].x * cell_size + cell_size / 4, path[x].y * cell_size + cell_size / 4,
                              cell_size / 2,
                              cell_size / 2])
        pygame.display.update()


def index(x_coordinate, y_coordinate, number_of_cell_each_row):
    if x_coordinate < 0 or x_coordinate >= number_of_cell_each_row or y_coordinate < 0 or y_coordinate >= number_of_cell_each_row:
        return None
    temp = x_coordinate + y_coordinate * number_of_cell_each_row

    return int(temp)


def get_neighbours_(cur, grid, number_of_cell_each_row):
    neighbours = []
    try:
        topi = index(cur.x, cur.y - 1, number_of_cell_each_row)
        top = grid[topi]
        if not cur.walls[0]:
            neighbours.append(top)
    except:
        pass

    try:
        righti = index(cur.x + 1, cur.y, number_of_cell_each_row)
        right = grid[righti]
        if not cur.walls[1]:
            neighbours.append(right)
    except:
        pass

    try:
        bottomi = index(cur.x, cur.y + 1, number_of_cell_each_row)
        bottom = grid[bottomi]
        if not cur.walls[2]:
            neighbours.append(bottom)
    except:
        pass

    try:
        lefti = index(cur.x - 1, cur.y, number_of_cell_each_row)
        left = grid[lefti]
        if not cur.walls[3]:
            neighbours.append(left)
    except:
        pass

    return neighbours


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
