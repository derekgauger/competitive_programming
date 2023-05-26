def search_and_fill(grid, i, j):
    rows = len(grid)
    columns = len(grid[0])
    # Check if position is connected to the '0' region
    # Can't be off the edge of the grid
    if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 0:
        return
    # Mark the region as connected
    grid[i][j] = -1
    # Search the connected cells
    search_and_fill(grid, i - 1, j)
    search_and_fill(grid, i + 1, j)
    search_and_fill(grid, i, j - 1)
    search_and_fill(grid, i, j + 1)


def coast_length(grid):
    rows = len(grid)
    columns = len(grid[0])
    # Create a new grid surrounded by water '0's
    new_rows = rows + 2
    new_columns = columns + 2
    new_grid = [[0 for _ in range(new_columns)] for _ in range(new_rows)]
    for i in range(rows):
        new_grid[i + 1][1:-1] = grid[i]
    
    # Flood fill the water point 0,0 is guaranteed to be water
    # Convert the surrounded grid into a graph
    # Use negative numbers to represent an edge since positive number are used for
    # indicating land
    search_and_fill(new_grid, 0, 0)

    # Every non-marked location contributes to the coastline
    # NOTE: Start at index 1 and end at (new_rows/new_columns) - 1 since
    # We know the new_grid is surrounded by 0
    coast = 0
    for i in range(1, new_rows - 1):
        for j in range(1, new_columns - 1):
            # Search for an isalnd mark
            # NOTE: Water was marked as '-1' in the search and flood
            if new_grid[i][j] == -1:
                continue

            # Found an isalnd segment check if it is bordered by water# If so, it is on the coast.
            if new_grid[i - 1][j] == -1:
                coast += 1
            
            if new_grid[i + 1][j] == -1:
                coast += 1
        
            if new_grid[i][j + 1] == -1:
                coast += 1

            if new_grid[i][j - 1] == -1:
                coast += 1
    return coast


def main():
    grid = [
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(coast_length(grid))

main()