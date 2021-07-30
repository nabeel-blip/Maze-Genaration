from CellClass import Cell
from searchingAlgorithm import *


def main():
    screen_size = (400, 400)
    number_of_cell_each_row = 32

    cell_size = int(screen_size[0] / number_of_cell_each_row)
    margin = 5

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
        # show_grid(screen, grid, cell_size)

        neighbours = get_neighbours(current, grid, number_of_cell_each_row)
        next = get_random_neighbour(neighbours)
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
    show_grid(screen, grid, cell_size,False)

    print("done")
    start = grid[0]
    goal = grid[len(grid) - 1]
    show_grid(screen, grid, cell_size,False)

    print_path2(a_star_candy(start, goal, grid, number_of_cell_each_row, screen, cell_size), screen, cell_size)

    print("done")

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
