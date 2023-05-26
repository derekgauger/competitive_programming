class TreeNode:
    
    def __init__(self, i):
        self.value = i
        self.left_child = None
        self.right_child = None
    
    # Inserts a value into the binary search tree
    # @param i the value to insert
    def insert(self, i):
        if i < self.value:
            if self.left_child is None:
                self.left_child = TreeNode(i)
            else:
                self.left_child.insert(i)
        else:
            if self.right_child is None:
                self.right_child = TreeNode(i)
            else:
                self.right_child.insert(i)
    
    # Search the tree for a value
    # @param i the value to find
    # @return - the node containing the value or null if not found
    def search_recursive(self, i):
        if i == self.value:
            return self
        if i < self.value and self.left_child is not None:
            return self.left_child.search_recursive(i)
        elif i > self.value and self.right_child is not None:
            return self.right_child.search_recursive(i)
        else:
            return None
    
    def check_valid(self, lower_bound, upper_bound):
        # The key with check valid - keep track of running upper and lower bound
        # at each level of the tree
        # If the value of the current node is below the lower bound or above the upper bound
        # then the tree is not valid
        if self.value <= lower_bound or self.value >= upper_bound:
            return False
        # Check the left and right subtrees adjusting the bounds appropriately
        left_child_valid = self.left_child is None or self.left_child.check_valid(lower_bound, self.value)
        right_child_valid = self.right_child is None or self.right_child.check_valid(self.value, upper_bound)
        return left_child_valid and right_child_valid
    
    
    # Prints the tree using the inorder traversal
    # @param spacing the spacing between tree levels
    def print_recursive(self, spacing):
        if self.right_child is not None:
            self.right_child.print_recursive(spacing + "   ")
        print(spacing + str(self.value))
        if self.left_child is not None:
            self.left_child.print_recursive(spacing + "   ")

class ValidatedBinarySearchTree:

    def __init__(self):
        self.root = None

    def find_node(self, i):
        if self.root is None:
            return None
        return self.root.search_recursive(i)

    def insert(self, i):
        if self.root is None:
            self.root = TreeNode(i)
        else:
            self.root.insert(i)

    def is_valid(self):
        if self.root is None:
            return True
        else:
            return self.root.check_valid(-1 + float('-inf'), 1 + float('inf'))

    def print(self):
        if self.root is not None:
            self.root.print_recursive("")

def main():
    # Construct a valid tree
    my_valid_tree = ValidatedBinarySearchTree()
    values1 = [10, 8, 12, 6, 9, 14, 13, 16]
    for value in values1:
        my_valid_tree.insert(value)

    my_valid_tree.print()
    print(my_valid_tree.is_valid())

    # Construct an invalid tree
    my_invalid_tree = ValidatedBinarySearchTree()
    values2 = [10, 8, 12, 6, 14, 13, 16]
    for value in values2:
        my_invalid_tree.insert(value)

    # Insert 15 in a bad place
    eight_node = my_invalid_tree.find_node(8)
    eight_node.right_child = TreeNode(15)

    my_invalid_tree.print()
    print(my_invalid_tree.is_valid())

main()