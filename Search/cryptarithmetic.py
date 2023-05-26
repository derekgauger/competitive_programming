import json

# ------------------------------------------------------------------
# Converts a string to an integer given a character -> Assignment map
# @param str - String to convert
# @param assignments - Caharacter -> value assignment map
# @return - The string as an integer
# ------------------------------------------------------------------
def string_to_int(str, assignments):
    value = 0
    magnitude = 1
    for i in reversed(range(len(str))):
        value += assignments[str[i]] * magnitude
        magnitude *= 10
    return value

# ------------------------------------------------------------------
# Checks a character -> value assignment map to see if it gives the correct
# answer to the problem
# @param operand1 - first operand
# @param operation - operation (must be either "+" or "*")
# @param operand2 - second operand
# @param answer - answer
# @param assignments - character -> value assignment map
# @return - true if arithmetic is correct - false if not
# ------------------------------------------------------------------
def check_answer(operand1, operation, operand2, answer, assignments):
    op1_int = string_to_int(operand1, assignments)
    op2_int = string_to_int(operand2, assignments)
    ans_int = string_to_int(answer, assignments)
    if operation == "+":
        return (op1_int + op2_int == ans_int)
    elif operation == "*":
        return (op1_int * op2_int == ans_int)
    return False

# ------------------------------------------------------------------
# Check if there are any characters that do not have an assigned numeric value
# @param assignments - character -> value map
# @return - a character from the map that does not have an assignment
# or null if all characters have an assignment
# ------------------------------------------------------------------
def check_assignment(assignments):
    for key, value in assignments.items():
        if value == None:
            return key
    return None

# ------------------------------------------------------------------
# Initialize the open list for each unique character in the problem
# @param operand1 - first operand
# @param operand2 - second operand
# @param answer - answer
# @return - the initialized open list with no values assigned to any character
# ------------------------------------------------------------------
def init_open_list(operand1, operand2, answer):
    # Create a new list
    open_list = []
    # Find unique characters from all operands and answer
    chars = {}
    for i in range(len(operand1)):
        chars[operand1[i]] = None

    for i in range(len(operand2)):
        chars[operand2[i]] = None

    for i in range(len(answer)):
        chars[answer[i]] = None
    
    # Add the characters to the open list
    # NOTE: No numerical assignments are given yet, that will come during search
    open_list.insert(0, chars)
    return open_list

# ------------------------------------------------------------------
# Given a character that has not been assigned a potential set of values (0-9)
# build items for the open list with each possible value assigned
# Skip a value if another member in the parent 'assignment' already has that value
# @param c - the character to give values
# @param assignment - the parent node assignment
# @param openList = The current open list
# @return - The open list with new appends
# ------------------------------------------------------------------
def append_assignments(c, assignments, open_list):
    for i in range(10):
        if not i in list(assignments.values()):
            new_assignment = dict(assignments)
            new_assignment[c] = i
            open_list.insert(0, new_assignment)
    return open_list

# ------------------------------------------------------------------
# Solve a cryparithmetic puzzle using search
# @param operand1 - first operand
# @param operation - operation (must be either "+" or "*")
# @param operand2 - second operand
# @param answer - answer
# @return - the assignments to all characters in operands and answer
# or null if a solution cannot be found
# ------------------------------------------------------------------
def solve(operand1, operation, operand2, answer):
    # Initialize the open list
    open_list = init_open_list(operand1, operand2, answer)
    # For each entry search for a solution
    while len(open_list) > 0:
        # Glab the first entry in the open list
        current_assignment = open_list.pop(0)
        # Check of all characters in the item have a numerical assignment
        unassigned = check_assignment(current_assignment)
        # At least one character does not have an assignment - add more elements to the open list
        if unassigned != None:
            open_list = append_assignments(unassigned, current_assignment, open_list)
        else:
            # All characters have an assignment, check arithmetic and return if correct
            if check_answer(operand1, operation, operand2, answer, current_assignment):
                return current_assignment
    return None

def main():
    solution = solve("SEND", "+", "MORE", "MONEY")
    if solution != None:
        print(json.dumps(solution, indent=4))
    else:
        print("No Solution")

main()