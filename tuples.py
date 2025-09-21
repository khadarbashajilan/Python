# 1. Swap two numbers using tuple unpacking
# ---------------------------------------
a, b = 5, 9          # before swap
a, b = b, a          # RHS creates tuple (b, a) → unpacked into a, b
# print(a, b)        # 9 5


# 2. Return multiple values from a function using tuples
# ------------------------------------------------------
def stats(seq):
    """Return min, max, and length of any iterable."""
    return min(seq), max(seq), len(seq)   # implicit 3-tuple

lo, hi, n = stats((3, 1, 4, 1, 5))
# print(lo, hi, n)   # 1 5 5


# 3. Count frequency of elements in a tuple
# -----------------------------------------
from collections import Counter
t = ('a', 'b', 'a', 'c', 'b', 'a')

def count_freq(t,e):
    count = 0
    for n in t:
        if n == e:
            count += 1
    print(count)

count_freq(t,t[1])

freq = Counter(t)    # Counter({'a': 3, 'b': 2, 'c': 1})

print(freq[t[1]])   # 3


# 4. Find the max and min in a tuple
# ----------------------------------
nums = (7, 2, 9, 4)
max_val = max(nums)  # 9
min_val = min(nums)  # 2
# print(max_val, min_val)


# 5. Convert list ↔ tuple
# -----------------------
lst = [1, 2, 3]
tpl = tuple(lst)     # list → tuple  (1, 2, 3)
back_to_list = list(tpl)  # tuple → list  [1, 2, 3]
# print(tpl, back_to_list)