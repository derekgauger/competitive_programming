def main():
    # 5 x 5 grid
    # Start at position 0, 0
    # End at position 4, 4
    # Obstacle in row 1, column 3
    # Obstacle in row 2, column 2

    # Initialize the counts
    rows = 5
    columns = 5
    # Initializing a 2-D array of length rows with arrays of length columns (All -1's)
    count = [[-1 for _ in range(columns)] for _ in range(rows)]
    # Across the first row there is one way to get to each position: move to the right
    for i in range(columns):
        count[0][i] = 1
    # Across the first column there is one way to get to each position: Move down
    for i in range(rows):
        count[i][0] = 1

    # It is not possible to get to a position with an obstacle
    count[1][3] = 0
    count[2][1] = 0
    
    # Across the rows and down the columns find the count for each cell
    for i in range(rows):
        for j in range(columns):
            if count[i][j] == -1:
                count[i][j] = count[i - 1][j] + count[i][j - 1]
    
    # Count in the lower right corner
    print(count[rows - 1][columns - 1])

main()