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

def portals(vertices, portals):
    max_portals = 2 * vertices
    # Best cost to reach each vertex
    costs = [float("inf")] * max_portals

    # Build adjacency list of edges
    edges = [[] for _ in range(max_portals)]
    for portal in portals:
        cost = portal[0]
        up = portal[1] - 1
        down = portal[2] - 1
        left = portal[3] - 1
        right = portal[4] - 1

        # an edge connecting up and down or connecting left and right has cost 0
        edges[up].append(Edge(up, down, 0))
        edges[down].append(Edge(down, up, 0))
        edges[left].append(Edge(left, right, 0))
        edges[right].append(Edge(right, left, 0))

        # Add the cost to reorder
        #   Since up,down and left,right are tied together only one change
        #   of direction is required
        edges[up].append(Edge(up, left, cost))
        edges[left].append(Edge(left, up, cost))

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

    cost = 0
    for edge in mst:
        cost += edge.weight
    return cost

def main():
    portals_data = [
        [10, 1, 4, 8, 9],
        [11, 1, 2, 5, 6],
        [12, 9, 10, 2, 3],
        [3, 4, 3, 6, 7],
        [15, 10, 8, 7, 5]
    ]
    print(portals(5, portals_data)) 


main()