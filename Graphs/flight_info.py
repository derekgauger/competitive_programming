import sys
from queue import PriorityQueue

MOD = 1000000007

class Flight:

    def __init__(self, dist, id):
        self.distance = dist
        self.identifier = id

    def __lt__(self, other):
        return self.distance < other.distance


def flight_info(cities, flights):
    # Build graph as adjacency list
    edges = [[] for _ in range(cities)]
    # Add flights as edges
    #   NOTE: vertices are 0 based but flights are 1 based
    for flight in flights:
        edges[flight[0] - 1].append(Flight(flight[2], flight[1] - 1))

    # Initialize the counting arrays
    distance = [sys.maxsize] * cities
    count = [1] * cities
    max_flights = [0] * cities
    min_flights = [0] * cities
    # Distance to the first city is 0 (no flights)
    distance[0] = 0

    # Run Dijkstra's keeping track of counts along the way
    open_list = PriorityQueue()
    open_list.put(Flight(0, 0))

    while not open_list.empty():
        curr = open_list.get()

        # if the node is already visited, ignore it
        if distance[curr.identifier] != curr.distance:
            continue

        for target in edges[curr.identifier]:
            count[target.identifier] %= MOD
            # if found shorter path, set the distance and reset counts
            if target.distance + distance[curr.identifier] < distance[target.identifier]:
                distance[target.identifier] = target.distance + distance[curr.identifier]
                count[target.identifier] = count[curr.identifier]
                max_flights[target.identifier] = max_flights[curr.identifier] + 1
                min_flights[target.identifier] = min_flights[curr.identifier] + 1
                
                open_list.put(Flight(distance[target.identifier], target.identifier))
            # with equivalent distance, update counts
            elif target.distance + distance[curr.identifier] == distance[target.identifier]:
                count[target.identifier] += count[curr.identifier];
                max_flights[target.identifier] = max(max_flights[target.identifier], max_flights[curr.identifier] + 1)
                min_flights[target.identifier] = min(min_flights[target.identifier], min_flights[curr.identifier] + 1)
            
    print(distance[cities - 1], count[cities - 1], min_flights[cities - 1], max_flights[cities - 1])


def main():
    cities = 4
    flights = [
        [1, 4, 5],
        [1, 2, 4],
        [2, 4, 5],
        [1, 3, 2],
        [3, 4, 3],
    ]
    flight_info(cities, flights)

main()