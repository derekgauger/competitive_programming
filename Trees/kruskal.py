class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.sizes = [1] * size
        self.count = size # number of sets

    # Find the set that an item belongs to and perform path compression
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item]) # Path compression
        return self.parent[item]

    # Join two sets
    def union(self, item1, item2):
        # Find the sets
        set1 = self.find(item1)
        set2 = self.find(item2)
        # Sets must be disjoint
        if set1 == set2:
            return

        # Merge by setting the parent
        # Smaller set becomes child of larger set
        if self.sizes[set1] > self.sizes[set2]:
            self.parent[set2] = set1
            self.sizes[set1] += self.sizes[set2]
        else:
            self.parent[set1] = set2
            self.sizes[set2] += self.sizes[set1]
        self.count -= 1

class Edge:
    def __init__(self, s, t, w):
        self.src = s
        self.tgt = t
        self.weight = w

    def __str__(self):
        return "[{}->{} : {}]".format(self.src, self.tgt, self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

def kruskal(vertices, edge_array):
    # Build an array of edges
    edges = [Edge(e[0], e[1], e[2]) for e in edge_array]
    # Sort the array by weight
    edges.sort()
    # List to hold all the edges in the minimal spanning tree
    mst = []
    # Union find structure for storing vertex sets
    nodes = UnionFind(vertices+1)
    # Search all the edges
    for edge in edges:
        # Find the vertex set
        x = nodes.find(edge.src)
        y = nodes.find(edge.tgt)
        # Don't connect the edge if it doesn't connect components
        if x == y:
            continue
        # Add the edge to the MST
        mst.append(edge)
        # Join the sets
        nodes.union(x, y)
        # Done when a single set of vertices exists
        if nodes.count == 1:
            break
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
    for i in kruskal(9, edges):
        print(i)

main()





