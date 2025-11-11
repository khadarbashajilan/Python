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

    def add_beg(self, data):
        # Add a new node with the given data to the beginning of the list
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            self.head = new_node
            new_node.next = curr

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
        # Return the length of the linked list
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def element_at(self, idx):
        # Return the element at the specified index
        n = self.length_l()
        if not self.head:
            return "No elements exist"
        elif idx < 0 or idx >= n:
            return "Not in range of indices"
        curr = self.head

        for _ in range(idx):
            curr = curr.next
        return curr.data

    def remove_n(self, data):
        # Remove the first occurrence of the specified data
        if not self.head:
            print("No elements exist")
            return

        if self.head.data == data:
            self.head = self.head.next
            print(f"Removed successfully {data}")
            return

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                print(f"Removed successfully {data}")
                return
            curr = curr.next
        print(f"Not Found {data}")
        return

    def middle_ele(self):
        # Print the middle element of the linked list
        if not self.head:
            print("Empty")
            return
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"The middle element is {slow.data}")

    def reverse(self):
        # Reverse the linked list
        if not self.head:
            print("Empty")
            return
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return

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

li.element_at(-2)
li.element_at(50)
li.element_at(4)

li.remove_n(20)
li.print_l()
li.add_beg(100)
li.print_l()
li.middle_ele()
li.reverse()
li.print_l()
