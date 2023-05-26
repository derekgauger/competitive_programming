from queue import PriorityQueue

class Edge:
    
    def __init__(self, s, t, w):
        self.src = s
        self.tgt = t
        self.weight = w

    def __str__(self):
        return "[{}->{} : {}]".format(self.src, self.tgt, self.weight)
    
    def __lt__(self, other):
        return self.weight < other.weight

def prim(vertices, edge_array):
    # Best cost to reach each vertex
    costs = [float("inf")] * vertices
    
    # Build adjacency list of edges
    edges = [[] for i in range(vertices)]
    for edge in edge_array:
        edges[edge[0]].append(Edge(edge[0], edge[1], edge[2]))
        edges[edge[1]].append(Edge(edge[1], edge[0], edge[2]))
    
    # Array list to hold all the edges in the minimal spanning tree
    mst = []
    
    # Initialize priority queue and cost list
    costs[0] = 0
    open_list = PriorityQueue()
    for edge in edges[0]:
        open_list.put(edge)
    
    # Prim's algorithm based on BFS
    while not open_list.empty():
        curr = open_list.get()
        if costs[curr.tgt] != 0:
            mst.append(curr)
            costs[curr.tgt] = 0
            for edge in edges[curr.tgt]:
                if costs[edge.tgt] > edge.weight:
                    open_list.put(edge)
                    costs[edge.tgt] = edge.weight
    return mst


def main():
    edges = [
        [0, 1, 4],
        [1, 3, 2],
        [1, 4, 5],
        [2, 4, 3],
        [2, 5, 6],
        [3, 4, 1],
        [3, 6, 8],
        [4, 5, 10],
        [4, 7, 9],
        [4, 8, 2],
        [6, 7, 7],
        [7, 8, 5]
    ]
    for i in prim(9, edges):
        print(i)


main()