def solve(capacity, item_count, values, weights):
    max_values = [[0 for _ in range(capacity + 1)] for _ in range(item_count + 1)]
    for item in range(1,item_count + 1):
        for weight in range(1, capacity + 1):
            # At each iteration of inner loop the available capacity of the knapsack increases
            # Decide whether to include a new item in the knapsack

            # Max value without including the item
            max_val_without_curr = max_values[item - 1][weight]
            # Value with the item - assume zero for now
            max_val_with_curr = 0
            # Get the weight of the item
            weight_of_curr = weights[item - 1] # NOTE: The item weights are 0 based but the loop counters are 1 based

            # Does the item fit?
            if weight >= weight_of_curr:
                # Ok so the item fits so get the total value if its added
                max_val_with_curr = values[item - 1] # NOTE: The item values are 0 based but the loop counters are 1 based
                # Adding the item reduces the capacity of the knapsack
                remaining_capacity = weight - weight_of_curr
                # The value after adding the item consists of:
                # value of the item + the value if the knapsack had the reduced capacity
                max_val_with_curr += max_values[item - 1][remaining_capacity]

            # Item fits, but is it worth adding?
            # Pick the largest of the values with or without adding the item
            max_values[item][weight] = max(max_val_without_curr, max_val_with_curr)
    return max_values


def recoverItems(capacity, item_count, values, weights, max_values):
    # Backtrack from the solution to determine which items are added
    remaining_value = max_values[item_count][capacity]
    remaining_weight = capacity
    item = item_count
    while item > 0 and remaining_value > 0:
        # Does removing the item affect the value of the row without the item
        if remaining_value != max_values[item - 1][remaining_weight]:
            # Yep, this item must be in the knapsack
            print(item - 1)
            # Reduce the remaining value and capcity and look again
            remaining_value -= values[item - 1]
            remaining_weight -= weights[item - 1]
        item -= 1


def main():
    capacity = 10
    item_count = 4
    values = [10, 40, 30, 50]
    weights = [5, 4, 6, 3]
    max_values = solve(capacity, item_count, values, weights)
    print(max_values)
    print(max_values[item_count][capacity])
    recoverItems(capacity, item_count, values, weights, max_values)

main()