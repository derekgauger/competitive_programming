def num_squares(n):
    # Counts of perfect squares needed to reach a number
    # index represents the number
    # value at the index represents the perfect square count
    counts = [0 for _ in range(n + 1)]
    counts[0] = 1
    
    # Initialize the open list
    open_list = []
    open_list.append(0)

    while len(open_list) > 0:
        # Remove the value from the open list
        # Build children for the search space by adding perfect squares
        # Stop building children after value is > n
        curr = open_list.pop(0)
        i = 1
        while curr + i*i <= n:
            # Only add the new value if it hasn't been seen yet
            if counts[curr + i*i] == 0:
                counts[curr + i*i] = counts[curr] + 1
                open_list.append(curr + i*i)

            # Found the value we are looking for?
            # Return the count of perfect squares
            if counts[n] != 0:
                return counts[n] - 1
            i += 1 
    return 0


def main():
    print(num_squares(12))

main()