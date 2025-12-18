A = [-3, 2, 4, -4, 0, 3, 2, 6, 7, 8]

def bubble_sort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            # Compare adjacent elements
            if arr[i-1] > arr[i]:
                # Swap elements if they are in the wrong order
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            # Compare current element with the previous one
            if arr[j-1] > arr[j]:
                # Swap elements if they are in the wrong order
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                # If the current element is in the correct position, break the inner loop
                break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            # Find the index of the minimum element in the unsorted part of the array
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr