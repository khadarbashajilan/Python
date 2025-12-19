A = [-3, 2, 4, -4, 0, 3, 2, 6, 7, 8]

def bubble_sort(arr):
    # Initialize the length of the array
    n = len(arr)
    # Flag to check if any swaps were made in a pass
    flag = True

    # Continue sorting until no swaps are made in a pass
    while flag:
        flag = False
        # Iterate through the array
        for i in range(1, n):
            # Compare adjacent elements
            if arr[i-1] > arr[i]:
                # Swap elements if they are in the wrong order
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    # Return the sorted array
    return arr

def insertion_sort(arr):
    # Initialize the length of the array
    n = len(arr)
    # Iterate through the array starting from the second element
    for i in range(1, n):
        # Iterate backwards through the sorted part of the array
        for j in range(i, 0, -1):
            # Compare current element with the previous one
            if arr[j-1] > arr[j]:
                # Swap elements if they are in the wrong order
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                # If the current element is in the correct position, break the inner loop
                break
    # Return the sorted array
    return arr

def selection_sort(arr):
    # Initialize the length of the array
    n = len(arr)
    # Iterate through the array
    for i in range(0, n):
        # Assume the current index is the minimum
        min_idx = i
        # Iterate through the unsorted part of the array
        for j in range(i+1, n):
            # Find the index of the minimum element in the unsorted part of the array
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # Return the sorted array
    return arr

def merge_sort(arr):
    # Base case: if the array has only one element, it is already sorted
    n = len(arr)
    if n == 1:
        return arr

    # Divide the array into two halves
    half = n // 2

    # Recursively sort the left and right halves
    L = merge_sort(arr[:half])
    R = merge_sort(arr[half:])

    # Initialize lengths of left and right halves
    l_len = len(L)
    r_len = len(R)

    # Initialize the sorted array with zeros
    sorted_arr = [0] * n
    l, r = 0, 0  # Initialize indices for left and right halves
    i = 0  # Initialize index for the sorted array

    # Merge the left and right halves into the sorted array
    while l < l_len and r < r_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    # Copy the remaining elements of left half, if any
    while l < l_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    # Copy the remaining elements of right half, if any
    while r < r_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    # Return the sorted array
    return sorted_arr




