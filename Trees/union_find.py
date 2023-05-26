class UnionFind:
    def init(self, size):
        self.parent = [i for i in range(size)]
        self.sizes = [1] * size
        # Initially all items are in their own set
        for i in range(size):
            self.parent[i] = i
            self.sizes[i] = 1

    # Find an item in the set - perform path compression
    # @param item: the item to find
    # @return: the set (root item)
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])  # Search and path compression
        return self.parent[item]
    
    # Union - join two sets
    # @param item1: an item in the first set
    # @param item2: an item in the second set
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
            self.parent[set1] = set2
            self.sizes[set2] += self.sizes[set1]
        else:
            self.parent[set2] = set1
            self.sizes[set1] += self.sizes[set2]
