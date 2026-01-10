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

        queue = deque([self.root])

        while queue:
            popped = queue.popleft()

            if popped.left is None:
                popped.left = new_node
                return
            else:
                queue.append(popped.left)
            
            if popped.right is None:
                popped.right = new_node
                return
            else:
                queue.append(popped.right)


    def preorder(self):
        """ DFS """
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

    def postorder(self):
        """Left -> Right -> Node"""

        if not self.root:
            return []

        stack1 = [self.root]
        stack2 = []
        result = []

        while  stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if curr.left:
                stack1.append(curr)
            
            if curr.right:
                stack1.append(curr)
        
        while stack2:
            result.append(stack2.pop().value)
        return result
    
    # Recusrive appraoch:
    def postorder_rec(self):
        if not self.root:
            return []
        
        result = []

        result += self.postorder_rec(self.root.left)
        result += self.postorder_rec(self.root.right)
        result.append(self.root.value)
        
        return result
    

    def level_order(self):
        """ BFS """
        if not self.root:
            return []
        
        queue = deque([self.root])
        result = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()

                if node:
                    level.append(node.value)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            result.append(level)

        return result

    def __str__(self):
        if not self.root:
            return "[]"

        queue = deque([self.root])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(str(curr.value))
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

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
print(ex.level_order())