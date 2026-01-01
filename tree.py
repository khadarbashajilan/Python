class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, value):
        """Insert a node in level order (BFS)"""
        if self.root is None:
            self.root = Node(value)
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)

    def height(self, node=None):
        """Calculate the height of the tree"""
        if node is None:
            node = self.root
        if node is None:
            return 0
        # Base case: leaf node
        if node.left is None and node.right is None:
            return 1
        # Recursive case
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return max(left_height, right_height) + 1

    def __str__(self):
        """Return a string representation of the tree in a visual format"""
        if self.root is None:
            return "Empty Tree"
        
        lines = []
        self._build_tree_string(self.root, "", "", lines)
        return "\n".join(lines)
    
    def _build_tree_string(self, node, prefix, children_prefix, lines):
        """Helper method to build tree string recursively"""
        if node is None:
            return
            
        # Add current node
        lines.append(f"{prefix}{node.value}")
        
        # Determine which children exist
        has_left = node.left is not None
        has_right = node.right is not None
        
        if has_left or has_right:
            if has_right:
                self._build_tree_string(node.left, children_prefix + "├── ", 
                                       children_prefix + "│   ", lines)
            else:
                self._build_tree_string(node.left, children_prefix + "└── ", 
                                       children_prefix + "    ", lines)
            
            if has_right:
                self._build_tree_string(node.right, children_prefix + "└── ", 
                                       children_prefix + "    ", lines)

    def is_complete(self):
        """Check if the tree is complete (all levels fully filled except possibly last)"""
        if self.root is None:
            return True

        queue = [self.root]
        found_none = False

        while queue:
            current = queue.pop(0)

            if current is None:
                found_none = True
            else:
                if found_none:
                    return False
                queue.append(current.left)
                queue.append(current.right)

        return True

    def is_perfect(self):
        """Check if the tree is perfect (all interior nodes have 2 children and all leaves same level)"""
        if self.root is None:
            return True

        # Calculate the depth
        depth = self.height() - 1

        # Check if the number of nodes is 2^(depth+1) - 1
        expected_nodes = (1 << (depth + 1)) - 1
        actual_nodes = self.count_nodes()

        return expected_nodes == actual_nodes

    def count_nodes(self, node=None):
        """Count the number of nodes in the tree"""
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_count = self.count_nodes(node.left) if node.left else 0
        right_count = self.count_nodes(node.right) if node.right else 0
        return 1 + left_count + right_count

    def to_array(self, include_none=False):
        """Return array representation of the tree (level order)"""
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
            elif include_none:
                result.append(None)
            # Remove trailing None values if not including None
            elif not include_none:
                continue

        # Remove trailing None values
        if include_none:
            while result and result[-1] is None:
                result.pop()
                
        return result

    # Core traversal methods (essential for understanding)
    def preorder_traversal(self, node=None):
        """Root, Left, Right"""
        if node is None:
            if self.root is None:
                return []
            return self.preorder_traversal(self.root)
        
        # Root
        result = [node.value]

        # Left
        if node.left:
            result += self.preorder_traversal(node.left)

        # Right
        if node.right:
            result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self, node=None):
        """Left, Root, Right"""
        if node is None:
            if self.root is None:
                return []
            return self.inorder_traversal(self.root)
        
        result = []

        # left
        if node.left:
            result = self.inorder_traversal(node.left)

        # root
        result.append(node.value)

        # right
        if node.right:
            result += self.inorder_traversal(node.right)
        return result

    def postorder_traversal(self, node=None):
        """Left, Right, Root"""
        if node is None:
            if self.root is None:
                return []
            return self.postorder_traversal(self.root)
        
        result = []
        # Left
        if node.left:
            result = self.postorder_traversal(node.left)

        # Right
        if node.right:
            result += self.postorder_traversal(node.right)

        # Root
        result.append(node.value)
        return result

    def level_order_traversal(self):
        """Breadth-First Search (BFS)"""
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def print_tree_info(self):
        """Print basic tree information"""
        print("Tree visual representation:")
        print(self)
        print("\nTree height:", self.height())
        print("Is complete?", self.is_complete())
        print("Is perfect?", self.is_perfect())
        print("Node count:", self.count_nodes())
        print("Array representation:", self.to_array())

        print("\nTraversals:")
        print("Preorder:", self.preorder_traversal())
        print("Inorder:", self.inorder_traversal())
        print("Postorder:", self.postorder_traversal())
        print("Level order:", self.level_order_traversal())

# Example usage for beginners
if __name__ == "__main__":
    # Create a simple binary tree
    print("="*50)
    print("Example 1: Simple Binary Tree")
    print("="*50)
    tree = BinaryTree(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.print_tree_info()

    # Test perfect tree
    print("\n" + "="*50)
    print("Example 2: Perfect Binary Tree")
    print("="*50)
    perfect_tree = BinaryTree(1)
    perfect_tree.insert(2)
    perfect_tree.insert(3)
    perfect_tree.insert(4)
    perfect_tree.insert(5)
    perfect_tree.insert(6)
    perfect_tree.insert(7)
    perfect_tree.print_tree_info()
    
    # Test unbalanced tree
    print("\n" + "="*50)
    print("Example 3: Unbalanced Tree")
    print("="*50)
    unbalanced = BinaryTree(1)
    unbalanced.root.left = Node(2)
    unbalanced.root.left.left = Node(3)
    unbalanced.root.left.left.left = Node(4)
    unbalanced.root.right = Node(5)
    unbalanced.print_tree_info()
    
    # Test empty tree
    print("\n" + "="*50)
    print("Example 4: Empty Tree")
    print("="*50)
    empty_tree = BinaryTree()
    print(empty_tree)