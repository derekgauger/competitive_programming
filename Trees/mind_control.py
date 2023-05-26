# https://open.kattis.com/problems/control

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.sizes = [1] * size
        # Initially all items are in their own set
        for i in range(size):
            self.parent[i] = i
            self.sizes[i] = 1

    # Find an item in the set - perform path compression
    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item]) # Search and path compression
        return self.parent[item]

    # Union - join two sets
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

def main():
    recipes = int(input())
    answer = 0
    # Union find to store where all the ingredients are
    items = UnionFind(500001)

    # Loop over all recipes
    for i in range(recipes):
        ingredients_count, *ingredients = map(int, input().split())
        current_size = 0

        # Find all the cauldrons that contain the ingredients 
        #   and add up the size
        cauldron = set()
        for ingredient in ingredients:
            # What set "cauldron" is the ingredient in
            cauldron_set = items.find(ingredient)

            # If the cauldron is already in our current mix, skip it
            if cauldron_set in cauldron:
                continue

            # Add the cauldron to the mix
            cauldron.add(cauldron_set)

            # Add up the total size
            current_size += items.sizes[cauldron_set]

        # Does our mix match the current recipe size?
        #   If no, throw it away and move on to the next ingredient
        if current_size != ingredients_count:
            continue

        # Found a potion we can make
        #   "mix" i.e. union the cauldrons together
        answer += 1
        prev_set = -1
        for cauldron_set in cauldron:
            if prev_set == -1:
                prev_set = cauldron_set
            items.union(cauldron_set, prev_set)
    print(answer)

main()