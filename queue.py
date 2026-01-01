class Queue:
    def __init__(self):
        """Initialize an empty queue using a list."""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue.
        Returns None if the queue is empty."""
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def peek(self):
        """Return the item at the front of the queue without removing it.
        Returns None if the queue is empty."""
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def __str__(self):
        """Return a string representation of the queue."""
        return str(self.queue)

# Example usage
if __name__ == "__main__":
    q = Queue()

    # Enqueue elements
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Queue after enqueue operations:", q)  # [1, 2, 3, 4]

    # Peek at front element
    print("Front element:", q.peek())  # 1

    # Dequeue elements
    print("Dequeued element:", q.dequeue())  # 1
    print("Dequeued element:", q.dequeue())  # 2

    print("Queue after dequeue operations:", q)  # [3, 4]

    # Check if queue is empty
    print("Is queue empty?", q.is_empty())  # False

    # Get queue size
    print("Queue size:", q.size())  # 2