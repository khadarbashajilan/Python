# Comprehensive Data Structures and Algorithms Roadmap

## Introduction

This roadmap provides a structured approach to mastering DSA concepts essential for product-based company interviews. Each phase includes theoretical foundations, prerequisites, and practical problem sets.

## Phase 0: Foundations (2 Days)

### Theoretical Concepts:

1. **Big O Notation**:
   - Definition: Mathematical notation to describe the upper bound of an algorithm's runtime
   - Common complexities: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
   - Time vs Space complexity
   - Worst-case vs Average-case analysis

2. **Recursion**:
   - Definition: A function that calls itself
   - Components: Base case, Recursive case
   - Call stack and memory usage
   - Tail recursion optimization

3. **Memory Usage**:
   - Stack vs Heap memory
   - Value types vs Reference types
   - Garbage collection basics

### Prerequisites:
- Basic programming knowledge (variables, loops, conditionals, functions)
- Understanding of basic data types (integers, strings, arrays)

### Practice Strategy:
- Analyze time and space complexity of every solution
- Understand how different algorithms scale with input size
- Practice converting iterative solutions to recursive ones and vice versa

## Phase 1: Arrays & Strings (7 Days)

### Theoretical Concepts:

1. **Arrays**:
   - Static vs Dynamic arrays
   - Array operations (access, search, insert, delete)
   - Time complexity of array operations
   - Memory allocation for arrays

2. **Strings**:
   - String manipulation techniques
   - String vs Character array
   - Common string operations (concatenation, substring, split)

3. **Prefix/Suffix Sums**:
   - Definition and use cases
   - Implementation techniques
   - Time and space tradeoffs

### Prerequisites:
- Completed Phase 0 (Foundations)
- Understanding of basic array operations

### Problem Sets:

#### Easy Problems:
1. Find Closest Number to Zero
2. Merge Strings Alternately
3. Roman to Integer
4. Is Subsequence
5. Best Time to Buy and Sell Stock
6. Longest Common Prefix
7. Summary Ranges
8. Remove Duplicates From Sorted Array
9. Remove Element
10. Merge Sorted Array

#### Medium Problems:
1. Best Time to Buy and Sell Stock II
2. Remove Duplicates From Sorted Array II
3. Sort Colors
4. Product of Array Except Self
5. H Index
6. Merge Intervals
7. Spiral Matrix
8. ZigZag Conversion
9. Rotate Image

### Revision Checkpoint:
- Can you solve array problems without extra space?
- Can you explain the tradeoffs between time and space complexity?
- Can you identify when sorting is needed?
- Can you implement prefix/suffix sums correctly?

## Phase 2: Hashmaps & Sets (4 Days)

### Theoretical Concepts:

1. **Hashing**:
   - Definition and purpose
   - Hash functions and their properties
   - Collision resolution techniques (chaining, open addressing)

2. **Hashmaps**:
   - Implementation details
   - Time complexity analysis (average case vs worst case)
   - Common operations (insert, delete, search)

3. **Sets**:
   - Definition and use cases
   - Set operations (union, intersection, difference)
   - Implementation using hash tables

### Prerequisites:
- Completed Phase 1 (Arrays & Strings)
- Understanding of basic array operations

### Problem Sets:

#### Easy Problems:
1. Jewels and Stones
2. Contains Duplicate
3. Ransom Note
4. Valid Anagram
5. Maximum Number of Balloons
6. Two Sum
7. Majority Element

#### Medium/Hard Problems:
1. Valid Sudoku
2. Group Anagrams
3. Longest Consecutive Sequence

### Revision Checkpoint:
- Can you identify when hashing is needed?
- Can you justify the space usage of your solution?
- Can you explain how hash collisions are handled?
- Can you implement a basic hashmap from scratch?

## Phase 3: Two Pointers & Sliding Window (6 Days)

### Theoretical Concepts:

1. **Two Pointer Technique**:
   - Definition and use cases
   - Left-right pointer approach
   - Fast-slow pointer technique

2. **Sliding Window**:
   - Definition and use cases
   - Fixed vs Variable window
   - Window expansion and shrink logic
   - Time complexity optimization

3. **Pattern Recognition**:
   - Identifying when to use two pointers
   - Identifying when to use sliding window
   - Common problem patterns

### Prerequisites:
- Completed Phase 2 (Hashmaps & Sets)
- Understanding of array operations

### Problem Sets:

#### Two Pointers Problems:
1. Squares of a Sorted Array
2. Reverse String
3. Two Sum II
4. Valid Palindrome
5. 3Sum
6. Container With Most Water
7. 3Sum Closest
8. 4Sum
9. Trapping Rain Water

#### Sliding Window Problems:
1. Maximum Average Subarray I
2. Max Consecutive Ones III
3. Longest Substring Without Repeating Characters
4. Longest Repeating Character Replacement
5. Minimum Size Subarray Sum
6. Permutation in String

### Revision Checkpoint:
- Can you explain the pointer movement logic?
- Can you convert a brute force solution to a sliding window approach?
- Can you identify when the sliding window technique is applicable?
- Can you solve problems with multiple pointers?

## Phase 4: Linked Lists, Stacks & Queues (6 Days)

### Theoretical Concepts:

1. **Linked Lists**:
   - Definition and structure
   - Singly vs Doubly linked lists
   - Time complexity analysis
   - Common operations (traversal, insertion, deletion)

2. **Stacks**:
   - Definition and use cases (LIFO)
   - Implementation using arrays and linked lists
   - Common operations (push, pop, peek)
   - Applications (function call stack, expression evaluation)

3. **Queues**:
   - Definition and use cases (FIFO)
   - Implementation using arrays and linked lists
   - Common operations (enqueue, dequeue)
   - Applications (BFS, scheduling)

### Prerequisites:
- Completed Phase 3 (Two Pointers & Sliding Window)
- Understanding of array operations

### Problem Sets:

#### Linked Lists Problems:
1. Remove Duplicates from Sorted List
2. Reverse Linked List
3. Merge Two Sorted Lists
4. Linked List Cycle
5. Middle of the Linked List
6. Remove Nth Node from End of List
7. Copy List with Random Pointer

#### Stacks Problems:
1. Baseball Game
2. Valid Parentheses
3. Evaluate Reverse Polish Notation
4. Daily Temperatures
5. Min Stack
6. Largest Rectangle in Histogram

### Revision Checkpoint:
- Can you reverse a linked list in-place?
- Can you explain the stack usage in each problem?
- Can you identify when a stack is the right data structure?
- Can you implement a stack using queues and vice versa?

## Phase 5: Binary Search (4 Days)

### Theoretical Concepts:

1. **Binary Search Algorithm**:
   - Definition and use cases
   - Time complexity analysis
   - Implementation steps

2. **Search Space Reduction**:
   - Definition and purpose
   - Condition-based binary search
   - Handling edge cases

3. **Rotated Arrays**:
   - Definition and properties
   - Finding pivot point
   - Modified binary search approach

### Prerequisites:
- Completed Phase 4 (Linked Lists, Stacks & Queues)
- Understanding of array operations

### Problem Sets:
1. Binary Search
2. Search Insert Position
3. First Bad Version
4. Valid Perfect Square
5. Search a 2D Matrix
6. Find Minimum in Rotated Sorted Array
7. Search in Rotated Sorted Array
8. Koko Eating Bananas

### Revision Checkpoint:
- Can you explain the binary search algorithm clearly?
- Can you define the search space and condition for each problem?
- Can you solve binary search problems on rotated arrays?
- Can you identify when binary search is applicable?

## Phase 6: Trees & Tries (8 Days)

### Theoretical Concepts:

1. **Trees**:
   - Definition and properties
   - Binary trees vs General trees
   - Tree traversal (DFS, BFS)
   - Time complexity analysis

2. **Binary Search Trees (BST)**:
   - Definition and properties
   - Insertion, deletion, search operations
   - Time complexity analysis

3. **Tries**:
   - Definition and use cases
   - Trie node structure
   - Common operations (insert, search, prefix search)

### Prerequisites:
- Completed Phase 5 (Binary Search)
- Understanding of recursion

### Problem Sets:
1. Invert Binary Tree
2. Maximum Depth of Binary Tree
3. Balanced Binary Tree
4. Diameter of Binary Tree
5. Same Tree
6. Symmetric Tree
7. Path Sum
8. Subtree of Another Tree
9. Level Order Traversal
10. Kth Smallest in BST
11. Validate BST
12. Lowest Common Ancestor
13. Implement Trie

### Revision Checkpoint:
- Can you solve tree problems using both recursive and iterative approaches?
- Can you explain the different traversal orders?
- Can you identify when a trie is the right data structure?
- Can you implement tree operations correctly?

## Phase 7: Advanced Topics (14 Days)

### Heaps:
- Definition and properties
- Min-heap vs Max-heap
- Heap operations (insert, delete, extract-min/max)
- Time complexity analysis

### Backtracking:
- Definition and use cases
- Backtracking vs Brute force
- Common patterns (subsets, permutations, combinations)
- Time complexity analysis

### Graphs:
- Definition and properties
- Graph representations (adjacency matrix, adjacency list)
- Graph traversal (DFS, BFS)
- Common algorithms (Dijkstra, Prim, Kruskal)

### Dynamic Programming:
- Definition and use cases
- Memoization vs Tabulation
- Common patterns (fibonacci, knapsack, LIS, LCS)
- Time complexity analysis

### Bit Manipulation:
- Definition and use cases
- Common bitwise operations
- Bitmasking techniques
- Time complexity analysis

## Weekly Study Plan (8 Weeks)

| Week | Focus Area | Key Topics |
|------|------------|------------|
| 1    | Foundations + Arrays | Big O, Arrays, Strings |
| 2    | Arrays + Hashmaps | Arrays, Hashmaps, Sets |
| 3    | Two Pointers + Sliding Window | Two Pointers, Sliding Window |
| 4    | Linked Lists + Stacks | Linked Lists, Stacks, Queues |
| 5    | Binary Search | Binary Search, Search Space Reduction |
| 6    | Trees + Tries | Trees, BST, Tries |
| 7    | Heaps + Backtracking | Heaps, Backtracking |
| 8    | Graphs + DP + Revision | Graphs, Dynamic Programming, Bit Manipulation |

## Final Interview Readiness Checklist

Before your interview:
1. [ ] Review all theoretical concepts
2. [ ] Practice explaining solutions clearly
3. [ ] Optimize solutions for time and space complexity
4. [ ] Conduct mock interviews with dry runs
5. [ ] Review common pitfalls and edge cases
6. [ ] Understand when to use each data structure
7. [ ] Practice explaining tradeoffs between different approaches

## Additional Resources

- LeetCode Premium (for problem explanations and patterns)
- NeetCode.io (for structured problem sets)
- AlgoExpert (for in-depth explanations)
- Grokking the Coding Interview (book)
- Cracking the Coding Interview (book)

This comprehensive roadmap provides a structured approach to mastering DSA concepts essential for product-based company interviews. Each phase includes detailed theoretical foundations, prerequisites, and practical problem sets to reinforce your understanding.