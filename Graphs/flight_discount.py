import sys
from queue import PriorityQueue
import math
FALSE = 0
TRUE = 1

class Flight:

    def __init__(self, c, id, u):
        self.cost = c
        self.identifier = id
        self.discount_used = u
    
    def __lt__(self, other):
        dx = self.cost - other.cost
        if dx == 0:
            return self.identifier < other.identifier
        return self.cost < other.cost

def flight_discount(cities, flights):
        # Build graph as adjacency list
    edges = [[] for _ in range(cities)]
    # Add flights as edges
    #   NOTE: vertices are 0 based but flights are 1 based
    for flight in flights:
        edges[flight[0] - 1].append(Flight(flight[2], flight[1] - 1, 0))

    # Initialize the counting arrays
    cost = [[0 for _ in range(2)] for _ in range(cities)]
    for i in range(cities):
        cost[i][0] = sys.maxsize
        cost[i][1] = sys.maxsize
    
    # Cost to the first city is 0 (no flights)
    cost[0][FALSE] = 0
    cost[0][TRUE] = 0

    # Run Dijkstra's keeping track of counts along the way
    open_list = PriorityQueue()
    open_list.put(Flight(0,0,0))

    while not open_list.empty():
        curr = open_list.get()

        # if the node is already visited, ignore it
        if cost[curr.identifier][curr.discount_used] != curr.cost:
            continue
        
        # Break out when we find the target node
        if curr.identifier == cities - 1:
            break
            
        for target in edges[curr.identifier]:
            # Haven't used the discount, try it now for all targets
            if curr.discount_used == FALSE:
                discount_cost = curr.cost + math.floor(target.cost / 2)
                if discount_cost < cost[target.identifier][1]:
                    cost[target.identifier][1] = discount_cost
                    open_list.put(Flight(discount_cost, target.identifier, TRUE))

            # Check the cost without using the discount
            if curr.cost + target.cost < cost[target.identifier][curr.discount_used]:
                cost[target.identifier][curr.discount_used] = curr.cost + target.cost
                open_list.put(Flight(curr.cost + target.cost, target.identifier, curr.discount_used))

    return cost[cities - 1][TRUE]

def main():
    cities = 3
    flights = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 7],
        [2, 3, 1],
        [2, 1, 5]
    ]
    print(flight_discount(cities, flights))

main()