def min_climbing_cost(cost):
    # Base Cases
    if len(cost) == 1:
        return cost[0]
    
    if len(cost) == 2:
        return min(cost[0], cost[1])
    
    # Set total cost starting on first stair or skipping to the next stair
    total = [0 for _ in range(len(cost))] # Initializing an array of nonezero length to 0s
    total[0], total[1] = cost[0], cost[1]

    # The rest of the stairs going up
    # Cost is based on the current position + the minimum of skipping or not
    for i in range(2, len(cost)):
        total[i] = cost[i] + min(total[i - 1], total[i - 2])
    
    # Cost of going up all the stairs is the value at the end of the array
    print(total)
    return total[-1]

def main():
    cost = [ 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 ]
    print(min_climbing_cost(cost))

main()