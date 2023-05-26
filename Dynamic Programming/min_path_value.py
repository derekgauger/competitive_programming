def main():
    # initialize matrix information
    matrix = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    m = len(matrix)
    n = len(matrix[0])
    # Initializing a 2-D array of length M containing arrays of length N (all 0's)
    path_costs = [[0 for _ in range(n)] for _ in range(m)]
    # Path from the upper left to the upper left is the same as the value of the matrix
    path_costs[0][0] = matrix[0][0]

    # Going down the first column, the only way to go is down
    for i in range(1, m):
        path_costs[i][0] = path_costs[i-1][0] + matrix[i][0]

    # Going across the first row, the only way to go is right
    for i in range(1, n):
        path_costs[0][i] = path_costs[0][i-1] + matrix[0][i]
    
    # For every other elemewnt, a choice can be made to go down or across.
    # Choose the minimum for each step
    for i in range(1, m):
        for j in range(1, n):
            path_costs[i][j] = min(path_costs[i][j - 1], path_costs[i - 1][j]) + matrix[i][j]
    
    # The result is the value at the lower left of the pathCosts
    print(path_costs)
    print(path_costs[m-1][n-1])

main()