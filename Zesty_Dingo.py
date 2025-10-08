class TreeNode:
    def __init__(self, left=None, right=None, val="*"):
        self.left = left
        self.right = right
        self.val = val
    
    def __str__(self):
        return self._str_helper(0)
    
    def _str_helper(self, level):
        # Indent based on level
        result = "  " * level + str(self.val) + "\n"
        
        # Recursively print left and right subtrees
        if self.left:
            result += self.left._str_helper(level + 1)
        if self.right:
            result += self.right._str_helper(level + 1)
            
        return result


def generate_trees(height):
    """
    Generate all possible binary trees of exactly the given height.
    Height is defined as the number of edges on the longest path from root to leaf.
    """
    if height == 0:
        # Base case: a tree with just a root node has height 0
        return [TreeNode()]
    
    # Recursive case
    trees = []
    
    # Generate all possible left and right subtrees
    for left_height in range(height):
        right_height = height - 1
        
        left_subtrees = generate_trees(left_height)
        right_subtrees = generate_trees(right_height)
        
        # Create all possible combinations of left and right subtrees
        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                trees.append(TreeNode(left=left_tree, right=right_tree))
    
    # Mirror case: left subtree with max height
    left_subtrees = generate_trees(height - 1)
    for left_tree in left_subtrees:
        for right_height in range(height - 1):
            right_subtrees = generate_trees(right_height)
            for right_tree in right_subtrees:
                trees.append(TreeNode(left=left_tree, right=right_tree))
    
    return trees


def count_trees(height):
    """Count the number of unique binary trees of exactly height h"""
    return len(generate_trees(height))


def main():
    height = int(input("Enter the height of the binary trees: "))
    
    trees = generate_trees(height)
    print(f"Number of binary trees with height {height}: {len(trees)}")
    
    # Print the trees if there aren't too many
    if len(trees) <= 10:
        for i, tree in enumerate(trees):
            print(f"\nTree {i+1}:")
            print(tree)
    else:
        print("\nToo many trees to display. Showing first 5:")
        for i in range(5):
            print(f"\nTree {i+1}:")
            print(trees[i])


if __name__ == "__main__":
    main()
