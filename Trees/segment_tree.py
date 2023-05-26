class SegmentTreeNode:
    def __init__(self, f, t):
        self.from_ = f
        self.to = t
        self.value = 0
        self.left = None
        self.right = None

class SegmentTree:

    def __init__(self, values):
        self.root = self.build(values, 0, len(values)-1)

    def build(self, values, l, r):
        if l > r:
            return None
        node = SegmentTreeNode(l, r)
        if l == r:
            node.value = values[l]
        else:
            m = (l + r) // 2
            node.left = self.build(values, l, m)
            node.right = self.build(values, m + 1, r)
            if node.left is not None:
                node.value += node.left.value
            if node.right is not None:
                node.value += node.right.value
        return node

    def query(self, l, r):
        return self.query_recursive(self.root, l, r)

    def query_recursive(self, node, l, r):
        if node is None:
            return 0
        # Range matches the node
        if l <= node.from_ and node.to <= r:
            return node.value
        # Range is outside the node value
        if node.to < l or node.from_ > r:
            return 0
        return self.query_recursive(node.left, l, r) + self.query_recursive(node.right, l, r)

    def update(self, i, value):
        self.update_recursive(self.root, i, value)

    def update_recursive(self, node, i, value):
        if node is None:
            return 0
        # Range is outside the node value
        if node.to < i or node.from_ > i:
            return node.value
        # Range matches the node
        if node.from_ == node.to:
            node.value = value
        else:
            node.value = self.update_recursive(node.left, i, value) + self.update_recursive(node.right, i, value)
        return node.value

    def print_tree(self):
        self.print_inorder(self.root, "")

    def print_inorder(self, node, padding):
        if node.left is not None:
            self.print_inorder(node.left, padding + "        ")
        print(padding + "[" + str(node.from_) + "," + str(node.to) + "," + str(node.value) + "]")
        if node.right is not None:
            self.print_inorder(node.right, padding + "        ")

def main():
    values = [1, 6, 3, 3, 5, 2, 11, 0]
    this_tree = SegmentTree(values)
    this_tree.print_tree()

    print(this_tree.query(2, 5))

    this_tree.update(5, 5)
    this_tree.print_tree()
    
    print(this_tree.query(2, 5))

main()