from collections import deque
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class BinaryTree:
    def __init__(self, root_value = None):
        self.root = Node(root_value) if root_value is not None else None

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return

        dq = deque([self.root])

        while dq:
            popped = dq.popleft()

            if popped.left is None:
                popped.left = new_node
                return
            else:
                dq.append(popped.left)
            
            if popped.right is None:
                popped.right = new_node
                return
            else:
                dq.append(popped.right)


    def preorder(self):
        """"Node -> Left -> Right"""
        if not self.root:
            return []
        
        stack = [self.root]
        result = []

        while stack:
            curr = stack.pop()

            result.append(curr.value)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return result
    # OR
    # Reccursive Approach :
    def preorder_rec(self, node):
        if node is None:
            return []
        result = []

        result.append(node.value)
        result += self.preorder_rec(node.left)
        result += self.preorder_rec(node.right)

        return result
    
    
    def inorder(self):
        """Left -> Node -> Right"""
        if not self.root:
            return []

        curr = self.root
        stack = []
        result = []

        while curr or stack:
            while curr :
                stack.append(curr)
                curr = curr.left
            
            popped = stack.pop()
            result.append(popped.value)

            if popped.right:
                curr = popped.right
        
        return result
    # OR
    # Recurrsive Approach :         
    def inorder_rec(self, curr):
        if curr is None:
            return []
        
        result = []
        
        result += self.inorder_rec(curr.left)
        result.append(curr.value)
        result += self.inorder_rec(curr.right)

        return result   


    def __str__(self):
        if not self.root:
            return "[]"

        dq = deque([self.root])
        result = []

        while dq:
            curr = dq.popleft()
            result.append(str(curr.value))
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)

        return "[" + ", ".join(result) + "]"

ex = BinaryTree()
ex.insert(1)
ex.insert(2)
ex.insert(3)
ex.insert(4)
ex.insert(5)
ex.insert(6)
ex.insert(7)
print(ex)
print(ex.preorder())
print(ex.inorder())