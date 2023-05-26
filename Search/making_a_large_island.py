def search_and_fill(grid, i, j, value):
    rows = len(grid)
    columns = len(grid[0])
    # Check if position is part of an island
    # Can't be off the edge of the grid
    # Isalnd are 1's not 0's
    if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
        return 0
    # Found an island segment, mark it with the value
    grid[i][j] = value
    # Search neighboring sells (add 1 for current)
    return (
        1 +
        search_and_fill(grid, i - 1, j, value) +
        search_and_fill(grid, i + 1, j, value) +
        search_and_fill(grid, i, j - 1, value) +
        search_and_fill(grid, i, j + 1, value)
        )


def largest_island(grid):
    rows = len(grid)
    columns = len(grid[0])
    sizes = []
    starting_id = 2
    id = starting_id

    # Build list of island sizes
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                sizes.append(search_and_fill(grid, i, j, id))
                id += 1
    
    # Didn't find any island sizes
    if id == starting_id:
        return 1
    # All grid cells == 1? i.e. One big island
    elif sizes[0] == rows * columns:
        return sizes[0]
    
    # Search for a '0' (not an isalnd)
    # That could be flipped, find its neighbors and add the size
    max_size = 1
    for i in range(rows):
        for j in range(columns):
            # Found a 0 grid location, find the neighbor islands
            if grid[i][j] == 0:
                # Datastructure for no duplicates
                neighbors = set()

                if i > 0 and grid[i-1][j] != 0:
                    neighbors.add(grid[i-1][j] - starting_id)
                if i < rows-1 and grid[i+1][j] != 0:
                    neighbors.add(grid[i+1][j] - starting_id)
                if j > 0 and grid[i][j-1] != 0:
                    neighbors.add(grid[i][j-1] - starting_id)
                if j < columns-1 and grid[i][j+1] != 0:
                    neighbors.add(grid[i][j+1] - starting_id)

                # For each neighbor add the size
                # NOTE: The size starts at 1 since the 0 will be flipped to a 1
                sum = 1
                for neighbor in neighbors:
                    sum += sizes[neighbor]

                # Record the greatest area
                if sum > max_size:
                    max_size = sum

    return max_size


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
    print(largest_island(grid))


main()