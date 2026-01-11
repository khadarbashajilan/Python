# heapq_guide.py - Comprehensive Guide to Python's heapq Module

import heapq

# =============================================
# INTRODUCTION TO HEAPQ
# =============================================
"""
heapq is a module in Python that provides functions to implement a min-heap.
A heap is a specialized tree-based data structure that satisfies the heap property:
- For any given node, the value is less than or equal to its children's values (min-heap)
- For any given node, the value is greater than or equal to its children's values (max-heap)

Heaps are commonly used to implement priority queues and for efficient sorting algorithms.
"""

# =============================================
# BASIC HEAP OPERATIONS
# =============================================

# Create a heap (min-heap by default)
heap = []

# heappush(heap, item) - Push item onto heap, maintaining heap invariant
heapq.heappush(heap, 5)  # Heap: [5]
heapq.heappush(heap, 3)  # Heap: [3, 5]
heapq.heappush(heap, 7)  # Heap: [3, 5, 7]

# heappop(heap) - Pop the smallest item from the heap, maintaining heap invariant
smallest = heapq.heappop(heap)  # Returns 3, Heap: [5, 7]

# Peek at the smallest element (without removing)
smallest = heap[0]  # Returns 5

# heapify(x) - Transform list x into a heap, in-place, in O(len(x)) time
data = [5, 3, 7, 1, 8]
heapq.heapify(data)  # data is now a heap: [1, 3, 7, 5, 8]

# =============================================
# ADVANCED HEAP OPERATIONS
# =============================================

# heappushpop(heap, item) - Push item on the heap, then pop and return the smallest item
# Equivalent to heappush(heap, item) followed by heappop(heap)
result = heapq.heappushpop(heap, 4)  # Heap: [4, 5, 7]

# heapreplace(heap, item) - Pop and return the smallest item, then push the new item
# Equivalent to heappop(heap) followed by heappush(heap, item)
result = heapq.heapreplace(heap, 2)  # Heap: [2, 5, 7]

# nlargest(n, iterable) - Return a list with the n largest elements from the dataset
data = [5, 3, 7, 1, 8]
largest = heapq.nlargest(2, data)  # [8, 7]

# nsmallest(n, iterable) - Return a list with the n smallest elements from the dataset
smallest = heapq.nsmallest(2, data)  # [1, 3]

# merge(*iterables) - Merge multiple sorted inputs into a single sorted output
heap1 = [1, 3, 5]
heap2 = [2, 4, 6]
merged = list(heapq.merge(heap1, heap2))  # [1, 2, 3, 4, 5, 6]

# =============================================
# PRIORITY QUEUE IMPLEMENTATION
# =============================================

# Using tuples for priority queues (priority, task)
priority_heap = []
heapq.heappush(priority_heap, (2, 'task1'))
heapq.heappush(priority_heap, (1, 'task2'))
heapq.heappush(priority_heap, (3, 'task3'))

# Process tasks in priority order
while priority_heap:
    priority, task = heapq.heappop(priority_heap)
    print(f"Processing {task} with priority {priority}")

# =============================================
# HEAP SORTING
# =============================================

# Using heap for sorting
data = [5, 3, 7, 1, 8]
heapq.heapify(data)
sorted_data = [heapq.heappop(data) for _ in range(len(data))]  # [1, 3, 5, 7, 8]
print(sorted_data)


data = [5, 3, 7, 1, 8]
neg_data = [-x for x in data]
heapq.heapify(neg_data)
sorted_dec = [-heapq.heappop(neg_data) for _ in range(len(neg_data))]  # [8, 7, 5, 3, 1]

# =============================================
# TIME COMPLEXITY
# =============================================
"""
Time Complexity of heapq operations:
- heappush: O(log n)
- heappop: O(log n)
- heapify: O(n)
- heappushpop: O(log n)
- heapreplace: O(log n)
- nlargest: O(n log k) where k is the number of largest elements requested
- nsmallest: O(n log k) where k is the number of smallest elements requested
- merge: O(n) where n is the total number of elements across all iterables
"""

# =============================================
# HEAP PROPERTIES
# =============================================
"""
Key properties of heaps:
1. Complete binary tree structure
2. For min-heap: parent <= children
3. For max-heap: parent >= children
4. Can be represented as an array where for any node at index i:
   - Left child: 2i + 1
   - Right child: 2i + 2
   - Parent: (i-1)//2
"""
