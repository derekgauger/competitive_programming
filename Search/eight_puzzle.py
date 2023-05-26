# Size of the grid
SIZE = 3

# ------------------------------------------------------------------
# Class for keeping track of the Puzzle Configurations and number of
# moves associated with getting to that state
# ------------------------------------------------------------------
class PuzzleState():
    def __init__(self, puzzle_config, moves):
        self.puzzle_config = puzzle_config
        self.moves = moves
    
# ------------------------------------------------------------------
# Create a puzzle as 2D array list from a 2D array
# @param grid - input grid
# @return - the puzzle as a 2D array list
# ------------------------------------------------------------------
def create_puzzle(grid):
    puzzle = []
    for i in range(SIZE):
        puzzle.append([])
        for j in range(SIZE):
            puzzle[i].append(grid[i][j])
    return puzzle

# ------------------------------------------------------------------
# Create a deep copy of a puzzle
# @param other - the puzzle to copy
# @return - the copied puzzle
# ------------------------------------------------------------------
def copy_puzzle(other):
    puzzle_copy = []
    for i in range(SIZE):
        puzzle_copy.append([])
        for j in range(SIZE):
            puzzle_copy[i].append(int(other[i][j]))
    return puzzle_copy

# ------------------------------------------------------------------
# Find the empty cell within a puzzle
# @param puzzle - the puzzle to search
# @return - the row/column of the empty cell
# ------------------------------------------------------------------
def get_empty_cell(puzzle):
    for i in range(SIZE):
        for j in range(SIZE):
            if(puzzle[i][j] == 0):
                return [i, j]
    return None

# ------------------------------------------------------------------
# Makes a move in the given puzzle.  There are 4 options: up, left, down, and right
# @param puzzle - the puzzle to make the moves to
# @param rowMove - the specific move to make for the row (up or down)
# @param columnMove - the specific move to make for the column (left or right)
# @param emptyCell - the location of the empty cell
# @return - a new puzzle with the move made
# ------------------------------------------------------------------
def make_move(puzzle, row_move, column_move, empty_cell):
    empty_row = empty_cell[0]
    empty_column = empty_cell[1]
    # Find the new location for the empty cell
    new_row = empty_row + row_move
    new_column = empty_column + column_move
    # Check that the move is still on the board
    if (new_row < 0) or (new_row >= SIZE) or (new_column < 0) or (new_column >= SIZE):
        return None
    # Make a copy of the puzzle
    new_puzzle = copy_puzzle(puzzle)
    temp = new_puzzle[empty_row][empty_column]
    replacement = new_puzzle[new_row][new_column]
    # Switch the values from the empty cell and the new cell
    new_puzzle[new_row][new_column], new_puzzle[empty_row][empty_column] = temp, replacement
    return new_puzzle

# ------------------------------------------------------------------
# Find the targets for the given puzzle configuration
# @param puzzle - the starting puzzle configuration
# @return - A list of puzzles that can be reached from this puzzle
# ------------------------------------------------------------------
def get_edge_targets(puzzle: PuzzleState):
    empty_cell = get_empty_cell(puzzle.puzzle_config)
    if empty_cell == None:
        return []
    
    # Possible moves are up, down, left, and right
    open_list = []
    up = make_move(puzzle.puzzle_config, -1, 0, empty_cell)
    if up != None:
        open_list.append(PuzzleState(up, puzzle.moves + "U"))
    
    left = make_move(puzzle.puzzle_config, 0, -1, empty_cell)
    if left != None:
        open_list.append(PuzzleState(left, puzzle.moves + "L"))

    down = make_move(puzzle.puzzle_config, 1, 0, empty_cell)
    if down != None:
        open_list.append(PuzzleState(down, puzzle.moves + "D"))

    right = make_move(puzzle.puzzle_config, 0, 1, empty_cell)

    if right != None:
        open_list.append(PuzzleState(right, puzzle.moves + "R"))
    
    return open_list


# ------------------------------------------------------------------
# Solve a puzzle given by the grid
# @param p - the puzzle to solve
# @return - the moves needed to solve the puzzle or 'impossible' if not possible
# ------------------------------------------------------------------
def solve_puzzle(puzzle):
    # Set the goal puzzle
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    goal_puzzle = create_puzzle(goal)

    # Create the starting puzzle grid
    start = create_puzzle(puzzle)
    # Intiialize the distance counting map to count the number of moves
    distances = {}
    distances[str(start)] = 0
    # Create the open list and start with the current locations
    open_list = []
    open_list.append(PuzzleState(start, ""))
    # Search for the target - goal configuration
    while len(open_list) > 0:
        curr = open_list.pop(0)
        # If the goal is found, return the number of steps
        if curr.puzzle_config == goal_puzzle:
            return curr.moves
        
        for target in get_edge_targets(curr):
            # Ignore this configuration if it's already been seen
            if str(target.puzzle_config) in distances.keys():
                continue
            # Compute the distance to this configuration and add to the open list
            distances[str(target.puzzle_config)] = distances[str(curr.puzzle_config)] + 1
            open_list.append(target)
    # If the solution has not been found in all posibility, return  impossible
    return "Impossible"


def main():
    grid = [
        [0, 8, 6],
        [7, 1, 4],
        [2, 5, 3]
    ]
    print(solve_puzzle(grid))

main()