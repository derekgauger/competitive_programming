def print_grid(grid):
    for row in grid:
        print('\t'.join(str(i) for i in row))
    print()

def search_and_fill(grid, i, j, value):
    rows = len(grid)
    columns = len(grid[0])

    # Check if position is connected to the 'O' region
    # Can't be off the edge of the grid
    if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 'O':
        return
    
    # Mark the region as connected
    grid[i][j] = value

    # Search the connected cells
    search_and_fill(grid, i - 1, j, value)
    search_and_fill(grid, i + 1, j, value)
    search_and_fill(grid, i, j - 1, value)
    search_and_fill(grid, i, j + 1, value)

def capture_regions(board):
    rows = len(board)
    columns = len(board[0])

    print_grid(board)

    for j in range(columns):
        # Search across the top row
        if board[0][j] == 'O':
            search_and_fill(board, 0, j, 'V')
        # Search across the bottom row
        if board[rows - 1][j] == 'O':
            search_and_fill(board, rows - 1, j, 'V')
    
    for i in range(columns):
        # Search across the left column
        if board[i][0] == 'O':
            search_and_fill(board, i, 0, 'V')
        # Search across the right column
        if board[i][columns - 1] == 'O':
            search_and_fill(board, i, columns - 1, 'V')
    
    print_grid(board)

    for i in range(rows):
        for j in range(columns):
            # Capture unmarked cells
            if board[i][j] == 'O':
                board[i][j] = 'X'
            # Restore marked cells
            if board[i][j] == 'V':
                board[i][j] = 'O'

def main():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    capture_regions(board)
    print_grid(board)

main()