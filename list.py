# Remove duplis fromm sorted arrays
nums = [0,1,1,2,2]

def rem_dup(nums):  # Function to remove duplicates from sorted array in-place
    i = 1  # Initialize pointer for unique elements
    for j in range(1, len(nums)):  # Iterate through array starting from second element
        if nums[j] != nums[i - 1]:  # Check if current element is different from previous unique element
            nums[i] = nums[j]  # Place unique element at current position
            i += 1  # Move pointer to next position
    return i  # Return count of unique elements
print(rem_dup(nums))
print(nums)


#Merge Sorted Array (#88)
arr1 = [1,2,5,8,0,0,0]  # Initialize first array with zeros at the end
arr2 = [2, 3, 10]  # Initialize second array
a = 4  # Length of actual elements in arr1
b = 3  # Length of actual elements in arr2

def mer_sortArr(nums1, nums2, m, n):  # Function to merge two sorted arrays
    midx = m-1  # Pointer for nums1
    nidx = n-1  # Pointer for nums2
    right = m + n -1  # Pointer for the end of nums1

    while nidx >= 0:  # Loop until all elements in nums2 are processed
        if midx >= 0 and nums1[midx] > nums2[nidx]:  # Compare elements
            nums1[right] = nums1[midx]  # Place larger element at the end
            midx -= 1  # Move nums1 pointer left
        else:
            nums1[right] = nums2[nidx]  # Place nums2 element at the end
            nidx -= 1  # Move nums2 pointer left
        right -= 1  # Move right pointer left
        
print(arr1)
mer_sortArr(arr1, arr2, a, b)
print(arr1)

# Move Zeroes :

def move_z(nums):

    # Two Pinter Technique (left and right):

    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left +=1

    # Brute Force :

    # idx = 0
    # for i in range(len(numbs)):
    #     if numbs[i] != 0:
    #         numbs[idx] = numbs[i]
    #         idx += 1
    
    # while idx < len(numbs):
    #     numbs[idx] = 0
    #     idx += 1


numbs = [0,1,0,3,12]
print(numbs)
move_z(numbs)
print(numbs)
