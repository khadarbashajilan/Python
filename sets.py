# Intersection of Two Arrays (LeetCode #349).

nums1 = [1,2,2,1]
nums2 = [2,2]


def intersection_arr(n1, n2):
    s= set()
    small = n1 if len(n1) < len(n2) else n2
    large = n2 if len(n2) > len(n1) else n1

    for n in small:
        if n in large:
            s.add(n)
    return list(s)

print(intersection_arr(nums1,nums2))
# OR
# print(list(set(nums1) & set(nums2)))


#Remove duplicates from a list using set.

l = [1,2,2,23,3,3,4,5,6]
print(list(set(l)))


#Check if two strings have common characters.

def common_str(s1, s2):
    s= ""
    for i in s1:
        if i in s2:
            s += i
    return s

print(common_str("abcdef", "efghi"))


#Find Union and Difference 

def set_operations(s1, s2):
    union = s1 | s2
    difference = s1 - s2
    return union, difference

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(set_operations(s1, s2))

