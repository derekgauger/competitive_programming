import sys
from queue import PriorityQueue

class Edge:
    def __init__(self, s, t, w):
        self.source = s
        self.target = t
        self.weight = w
    
    def __lt__(self, other):
        return self.weight < other.weight

def dijkstra(vertices, edge_array, source, target):
    # Best cost to reach each vertex
    distances = [sys.maxsize] * vertices
    visited = [False] * vertices
    # Build adjacency list of edges
    edges = []
    for i in range(vertices):
        edges.append(PriorityQueue())
    # NOTE edges are 0 based but cities are 1 based
    for edge in edge_array:
        edges[edge[0] - 1].put(Edge(edge[0] - 1, edge[1] - 1, edge[2]))
    # Build an open list starting from the source
    open_list = [source - 1]
    distances[source - 1] = 0  # distance to source node is zero
    while len(open_list) > 0:
        curr = open_list.pop(0)

        # Optimization:
        # Can stop if we found the target
        # if we are only concerned about distance from source -> target
        
        #     if curr == target-1:
        #         break;
    
        # Skip the node if we've already visited it

        if visited[curr]:
            continue
        visited[curr] = True
        pq = edges[curr]
        while not pq.empty():
            edge = pq.get()
            if distances[edge.target] > distances[curr] + edge.weight:
                distances[edge.target] = distances[curr] + edge.weight
            open_list.append(edge.target)
    return distances[target - 1]

def main():
    vertices = 6
    edges = [
        [1, 2, 1],
        [1, 5, 5],
        [2, 3, 5],
        [2, 5, 3],
        [3, 4, 1],
        [4, 5, 5],
        [4, 6, 2]
    ]
    print(dijkstra(vertices, edges, 1, 6))

main()