def grid_steps(n, x, y):
    # Initialize the search grid
    grid = [[-1 for _ in range(n)] for _ in range(n)]
    grid[x][y] = 0

    # Initialize the open list with the start location
    open_list = [(x, y)]
    while len(open_list) > 0:
        # Pull an element off the open list queue
        curr = open_list.pop(0)
        row = curr[0]
        column = curr[1]

        # Check to see if neighbors have been seen yet,
        # If not, set the step count and add to the open list for search
        if row > 0 and grid[row - 1][column] == -1:
            grid[row - 1][column] = grid[row][column] + 1
            open_list.append((row - 1, column))
        
        if row < n - 1 and grid[row + 1][column] == -1:
            grid[row + 1][column] = grid[row][column] + 1
            open_list.append((row + 1, column))

        if column > 0 and grid[row][column - 1] == -1:
            grid[row][column - 1] = grid[row][column] + 1
            open_list.append((row, column - 1))

        if column < n - 1 and grid[row][column + 1] == -1:
            grid[row][column + 1] = grid[row][column] + 1
            open_list.append((row, column + 1))
        
    return grid

def main():
    grid = grid_steps(5, 1, 2)
    print(grid)

main()