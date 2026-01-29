import math
# 1. Count Digits using modulo :

def count_digits_usingDiv(n):
    n = abs(n)
    res = 0
    while n > 0 :
        n //= 10
        res += 1
    
    return res 

# 1. Count Digits using log :

def count_dig_usingLog(n) :
    if n == 0: return 1
    n = abs(n)
    return math.floor(math.log10(n)) + 1

# print(count_digits_usingDiv(1674))
# print(count_dig_usingLog(1674))


# 3. Extracting each digit of a number :

def extract_eachDig(n):
    n = abs(n)
    arr = []
    while n > 0:
        arr.append(n % 10)
        n //= 10
    return arr

# print(extract_eachDig(1234))

# 4. Appending a digit to a number :

def append_dig(n,d):
    if n == 0 : return d

    ans = (abs(n) *10) + d
    
    return ans if n >= 0 else -ans

# print(append_dig(-125, 2))

# 5. Insert a digit at the front of a number :

def insert_digFront(n,d):
    if n== 0 : return d

    length = math.floor(math.log10(abs(n))) + 1

    for _ in range(length):
        d *= 10
    
    return d + n if n > 0 else (d + abs(n)) * -1 

# print(insert_digFront(-1245, 8))


# 6. Reverse the digits of a number :

def reverse_num(n):
    rev = 0
    isNegative = n < 0
    n_abs = abs(n)

    while n_abs > 0:
        ld = n_abs % 10
        rev = rev *10 + ld
        n_abs //= 10
    
    return rev if not isNegative else rev * -1

# print(reverse_num(-541))
# print(reverse_num(0))


# 7. power of number  (using memo + dp):
# O(p) - TC / SC

def power_n(n,p): 
    if p == 0 : return 1
    if n == 0 : return 0

    abs_p = abs(p)
    dp = {0:1}

    for i in range(1, abs_p+1):
        dp[i] = (dp[i-1] * n)
        
    return dp[abs_p] if p > 0 else 1 / dp[abs_p]

print(power_n(2,-2))
