# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        # Initialize a new node with data and next pointer
        self.data = data    # Store the value/data in this node
        self.next = None    # Pointer to the next node (initially None)

# Define a LinkedList class to manage the entire list
class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None    # Head pointer points to the first node (initially None for empty list)
    
    def append(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)  # Create a new node with the given data
        
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node  # New node becomes the first node
            return
        
        # If list is not empty, traverse to the end
        curr = self.head    # Start from the head node
        while curr.next:    # Continue until we reach the last node (where next is None)
            curr = curr.next  # Move to the next node
        
        # Add the new node at the end
        curr.next = new_node  # Link the last node to the new node

    def print_l(self):
        # Print all elements in the linked list
        curr = self.head    # Start from the head node
        while curr:         # While current node exists (not None)
            print(curr.data, end=" -> ")  # Print current node's data with arrow
            curr = curr.next  # Move to the next node
        print("None")       # Print None to indicate end of list

    def length_l(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

# Create a linked list instance
li = LinkedList()

# Add elements to the linked list
li.append(10)  # List becomes: 10 -> None
li.append(20)  # List becomes: 10 -> 20 -> None  
li.append(30)  # List becomes: 10 -> 20 -> 30 -> None

# Print the entire linked list
li.print_l()   # Output: 10 -> 20 -> 30 -> None
print(li.length_l())

li.append(40)
li.append(50)
li.print_l()
print(li.length_l())


