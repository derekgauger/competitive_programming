import time

class Segment_Tree_Array:

    def __init__(self, values):
        self.tree = [0] * (len(values) * 2)
        self.value_count = len(values)
        # Add leaf nodes
        self.tree[self.value_count:self.value_count*2] = values[:]
        # build the tree by calculating parents
        for i in range(self.value_count - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        temp_index = index + self.value_count
        # set value at position
        self.tree[temp_index] = value
        # move upward and update parents
        i = temp_index
        while i > 1:
            # Add left and right children to get parent value
            if i % 2 == 0:
                self.tree[i // 2] = self.tree[i] + self.tree[i + 1]
            else:
                self.tree[i // 2] = self.tree[i] + self.tree[i - 1]
            i //= 2

    def query(self, l, r):
        sum = 0
        # Start at the leaf nodes and find the highest parent
        temp_left = l + self.value_count
        temp_right = r + self.value_count + 1

        while temp_left < temp_right:
            # If node is not subsumed by parent
            #    include its value in the sum
            if temp_left % 2 == 1:
                sum += self.tree[temp_left]
                temp_left += 1
            if temp_right % 2 == 1:
                temp_right -= 1
                sum += self.tree[temp_right]

            temp_left //= 2
            temp_right //= 2

        return sum

    def print_tree(self):
        print(self.tree)

def main():
    values = [1, 6, 3, 3, 5, 2, 11, 0]

    start = time.perf_counter_ns()
    this_tree = Segment_Tree_Array(values)
    this_tree.print_tree()
    print(this_tree.query(2, 5))

    this_tree.update(5, 5)
    this_tree.print_tree()
    print(this_tree.query(2, 5))
    end = time.perf_counter_ns()
    print("TIME: " + str(end - start))


main()