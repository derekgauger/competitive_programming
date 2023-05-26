def search(grid, i, j):
    rows = len(grid)
    columns = len(grid[0])

    # Check if position is part of an island
    # Can't be off the edge of the grid
    # Islands are 1's not 0's
    if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
        return 0
    
    # Found an island segment, mark it as viewed
    grid[i][j] = 2
    
    # Search neighborcells and add 1 since this is also an island
    return (
            1 +
            search(grid, i - 1, j) +
            search(grid, i + 1, j) +
            search(grid, i, j - 1) +
            search(grid, i, j + 1)
            )


def max_area_of_island(grid):
    rows = len(grid)
    columns = len(grid[0])
    max_island = 0
    # Search the grid for islands
    for i in range(rows):
        for j in range(columns):
            # Island found, find the area
            if grid[i][j] == 1:
                island_area = search(grid, i, j)
                if island_area > max_island:
                    max_island = island_area
    return max_island

def main():
    grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
    print(max_area_of_island(grid))

main()