from re import L
import sys
from queue import PriorityQueue
# Direction of the turtle
#    0 -> up, 1 -> right, 2 -> down, 3 -> left
# Helper arrays for the offset to the next row or column
#    based on current turtle direction
# up (value of 0) reduces the row by 1 but leave the column the same
# right (value of 1) leaves the row the same but increases the column by 1
# down (value of 2) increases the row by 1 but leaves the column the same
# left (value of 3) leaves the row the same but reduces the column by 1
NEXT_ROW = [-1, 0, 1, 0]
NEXT_COLUMN = [0, 1, 0, -1]

class State:
    def __init__(self, i, j, dir, dst, m):
        self.row = i
        self.column = j
        self.direction = dir
        self.distance = dst
        self.moves = m
    
    def __lt__(self, other):
        return self.distance < other.distance

def robot_turtles(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the distance array
    #   First index -> turtle orientation
    #      0 -> up, 1 -> right, 2 -> down, 3 -> left
    #   Second index is row
    #   Third index is column
    #   Element distances are initially infinity
    distances = [[[sys.maxsize for _ in range(8)] for _ in range(8)] for _ in range(4)]
    # Set turtle's initial location
    #    bottom row - 7
    #    left column - 0
    #    facing right - 1
    distances[1][7][0] = 0
    open_list = PriorityQueue()
    open_list.put(State(7, 0, 1, 0, ""))

    # Run Dijkstra's to search for the end square 'D'
    while not open_list.empty():
        curr = open_list.get()

        if curr.distance != distances[curr.direction][curr.row][curr.column]:
            continue

        if grid[curr.row][curr.column] == 'D':
            return curr.moves

        # Check possible new locations to search

        # Move forward
        new_row = curr.row + NEXT_ROW[curr.direction]
        new_column = curr.column + NEXT_COLUMN[curr.direction]
        in_grid = new_row >= 0 and new_row < rows and new_column >=0 and new_column < cols 

        # new location must be in the grid and a space that the turtle can occupy
        if in_grid and (grid[new_row][new_column] == '.' or grid[new_row][new_column] == 'D'):
            # Is the ove worth it in terms of distance?
            if distances[curr.direction][curr.row][curr.column] + 1 < distances[curr.direction][new_row][new_column]:
                # Set new distance
                distances[curr.direction][new_row][new_column] = distances[curr.direction][curr.row][curr.column] + 1
                # Add the target to the open list
                open_list.put(State(new_row, new_column, curr.direction, distances[curr.direction][new_row][new_column], curr.moves + "F"))

        # melt ice castle and move forward
        if in_grid and grid[new_row][new_column] == 'I':
            # Is the move worth it in terms of distance
            if distances[curr.direction][curr.row][curr.column] + 2 < distances[curr.direction][new_row][new_column]:
                # Set the new distance
                distances[curr.direction][new_row][new_column] = distances[curr.direction][curr.row][curr.column] + 2
                # Add the target to the openlist
                open_list.put(State(new_row, new_column, curr.direction, distances[curr.direction][new_row][new_column], curr.moves + "XF"))

        # turn left or right
        for turn in [-1, 1]:
            new_direction = (curr.direction + turn + 4) % 4
            if turn == -1:
                new_move = "L"
            else:
                new_move = "R"
            
            # Is the move worth it in terms of distance?
            if distances[curr.direction][curr.row][curr.column] + 1 < distances[new_direction][curr.row][curr.column]:
                # Set new distance
                distances[new_direction][curr.row][curr.column] = distances[curr.direction][curr.row][curr.column] + 1
                # Add the target to the open list
                open_list.put(State(curr.row, curr.column, new_direction, distances[new_direction][curr.row][curr.column], curr.moves + new_move))
        
    # Search is done if we get here then there must not be a solution
    return "no solution"

def main():
    grid = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        line = [*input()]
        for j in range(8):
            grid[i][j] = line[j]
    print(robot_turtles(grid))
main()