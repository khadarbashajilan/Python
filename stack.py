class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None
        return print(self.stack.pop())

    def peek(self):
        if not self.stack:
            print("Stack is empty")
            return None
        return print(self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)
    
# Test Case 1: Basic push and pop operations
print("\nTest Case 1: Basic push and pop operations")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
# Expected output: 3 (peek), 3 (pop), 2 (pop), 1 (pop)
s.peek()  # Should print 3
s.pop()   # Should print 3
s.pop()   # Should print 2
s.pop()   # Should print 1

# Test Case 2: Pop from empty stack
print("\nTest Case 2: Pop from empty stack")
s = Stack()
s.pop()  # Should print "Stack is empty" and return None

# Test Case 3: Peek from empty stack
print("\nTest Case 3: Peek from empty stack")
s = Stack()
s.peek()  # Should print "Stack is empty" and return None

# Test Case 4: Mixed operations
print("\nTest Case 4: Mixed operations")
s = Stack()
s.push(10)
s.push(20)
s.peek()  # Should print 20
s.push(30)
s.pop()   # Should print 30
s.peek()  # Should print 20
s.pop()   # Should print 20
s.pop()   # Should print 10
s.pop()   # Should print "Stack is empty" and return None

#  Test Case 5: is_empty check
print("\nTest Case 5: is_empty check")
s = Stack()
print(s.is_empty())  # Should print True
s.push(1)
print(s.is_empty())  # Should print False
s.pop()
print(s.is_empty())  # Should print True
