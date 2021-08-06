from HelperFunctions import *
from copy import deepcopy


def actual_coordinates(x, y, cell_size):
    return x * cell_size, y * cell_size


def debug(x):
    print(x.x, x.y)


def GetH(neighbour, goal):
    return abs(neighbour.x - goal.x) + abs(neighbour.y - goal.y)


def a_star_candy(starting, goal, grid, number_of_cell_each_row, screen, cell_size):
    queue = [([starting], 0)]
    visited = [starting]
    while queue:
        pygame.event.get()

        # Dequeue a vertex from
        # queue and print it
        queue.sort(key=lambda t: t[1])  # sort for GbestFS and A*

        current = queue.pop(0)
        if current[0][-1] == goal:
            show_grid(screen, grid, cell_size, False)
            return current[0]
        #   temp = calculate_actual_cost(current[0])
        #        return current[0], temp

        for neighbour in get_neighbours_(current[0][-1], grid, number_of_cell_each_row):  # for ever neighbour
            if neighbour not in visited:  # which is not in visited
                temp = deepcopy(current[0])
                temp.append(neighbour)
                new_path = (temp, len(current[0]) + GetH(neighbour, goal))
                queue.append(new_path)
                visited.append(neighbour)
                neighbour.highlight = True
                neighbour.show(screen, cell_size)
                pygame.display.update()


def DFS_r(grid, current, goal, number_of_cell_each_row, screen, cell_size, visited=None, exit_key=False):
    if visited is None:
        exit_key = True
        visited = []

    if current == goal:
        if current not in visited:
            visited.append(current)
        return True
    x = False
    if current not in visited:
        # print(current)
        visited.append(current)
        current.highlight = True
        current.show(screen, cell_size)
        pygame.display.update()

        for neighbour in get_neighbours_(current, grid, number_of_cell_each_row):
            x = DFS_r(grid, neighbour, goal, number_of_cell_each_row,screen,cell_size, visited)

            if isinstance(x, bool):
                if x:
                    x = [current, neighbour]
                    break
            else:
                x.insert(0, current)
                break
    if exit_key:
        show_grid(screen, grid, cell_size, False)

        return x
    else:
        return x
