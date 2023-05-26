import math

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

class Point:
    def __init__(self, i, j):
        self.x = i
        self.y = j

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

class Edge:
    def __init__(self, s, t, w):
        self.src = s
        self.tgt = t
        self.weight = w

    def __lt__(self, other):
        return self.weight < other.weight

def main():
    tests = int(input())
    for k in range(tests):
        satellite_count, outpost_count = map(int, input().split(" "))
        
        # Zero distance needed if satellites equals outputs
        if satellite_count == outpost_count:
            print("0.00")
            continue
        
        # Build a list of outputs
        outposts = []
        for i in range(outpost_count):
            i, j = map(int, input().split(" "))
            outposts.append(Point(i, j))

        # Build an array of edges - distance between outputs indicates edge weight
        edges = []
        for i in range(outpost_count-1):
            for j in range(i+1, outpost_count):
                edges.append(Edge(i, j, distance(outposts[i], outposts[j])))

        # Run Kruskal's to find minimal spanning tree
        edges.sort()

        # Array list to hold all the edges in the minimal spanning tree
        mst = []
        nodes = UnionFind(outpost_count)

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
        
        # Remove edges from MST for each satellite
        #  NOTE: removing an edge counts for 2 nodes
        #        so start at 1 to avoid removing too many
        for i in range(1, satellite_count):
            mst.pop()

        # Print out the distance
        print("{:.2f}".format(mst.pop().weight))


main()
