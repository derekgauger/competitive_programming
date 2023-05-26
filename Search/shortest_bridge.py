def print_grid(grid):
    for row in grid:
        print('\t'.join(str(i) for i in row))
    print()


def search_and_fill(grid, i, j, open_list):
    rows = len(grid)
    columns = len(grid[0])

    # Check if position is connected to the 'O' region
    # Can't be off the edge of the grid
    if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
        return
    
    # Mark the region as connected
    grid[i][j] = -1
    # Add grid location to open list
    open_list.append((i, j))
    # Search the connected cells
    search_and_fill(grid, i - 1, j, open_list)
    search_and_fill(grid, i + 1, j, open_list)
    search_and_fill(grid, i, j - 1, open_list)
    search_and_fill(grid, i, j + 1, open_list)

def shortest_bridge(grid):
    found_island = False
    rows = len(grid)
    columns = len(grid[0])

    # search for and fill the first island
    open_list = []
    for i in range(rows):
        if not found_island:
            for j in range(columns):
                if not found_island:
                    if grid[i][j] == 1:
                        # Island found, fill the island and build open list for
                        # breadth first search
                        search_and_fill(grid, i, j, open_list)
                        found_island = True
    
    # TRICK - using an offset array can
    # reduce the amount of if statements needed
    # Here there are 4 neighbor cells with offset in row and column
    offset_row = [-1, 0, 1, 0]
    offset_column = [0, 1, 0, -1]
    direction_count = 4
    print_grid(grid)

    # Starting at the island found, search for the open island
    while len(open_list) > 0:
        # Pull an element off the search list
        curr = open_list.pop(0)
        row = curr[0]
        column = curr[1]
        print(curr)
        # Check to see if neighbors have been set yet
        # If not, set the step count and add to open list for search
        # NOTE: negative numbers used to indicate step counts
        # since islands are marked with positive numbers
        for i in range(direction_count):
            # Calculate the neighbor coordinate
            neighbor_row = row + offset_row[i]
            neighbor_column = column + offset_column[i]

            # Check if neighbor is in the grid
            if 0 <= neighbor_row and neighbor_row < rows and 0 <= neighbor_column and neighbor_column < columns:
                # Neighbor is in the grid, check if it is water ('0')
                # and mark the offset distance
                if grid[neighbor_row][neighbor_column] == 0:
                    grid[neighbor_row][neighbor_column] = grid[row][column] - 1
                    open_list.append((neighbor_row, neighbor_column))
                # Check of neighbors is an island, then we've found the shortest
                # distance, return it
                elif grid[neighbor_row][neighbor_column] == 1:
                    return (-1 * grid[row][column]) - 1
        print_grid(grid)
    # Empty open list, must not have found the other island
    return -1


def main():
    grid = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,0,0,1,0,0],
            [1,0,0,1,0,0,0,1,0,1],
            [1,0,0,1,0,0,0,1,1,1],
            [0,0,0,1,0,0,0,0,1,0],
            [0,0,0,1,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0,0,0]]
    print(shortest_bridge(grid))

main()