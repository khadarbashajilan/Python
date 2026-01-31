import math

# 1. Armstrong number

def isArmstrong_num(n):
    """A number is called a Armstrong number, if ex : n = 12,  number of digits in n is 2. If (1^2 + 2^2 == n  -> called Armstrong) """
    if n < 0 : return False
    copy = n
    count_digits = math.floor(math.log10(n)+1)
    res = 0.0
    while n > 0:
        ld = n % 10
        res += ld ** count_digits
        n //= 10
    return res == copy

# print(isArmstrong_num(153)) # True


# 2. Palindrome Number

def isPalindrome(n):
    if n < 0 : return False
    copy = n
    rev = 0
    while n > 0:
        ld = n % 10
        rev = rev * 10 + ld 
        n //= 10
    return copy == rev



# 3. Print all divisors :

def printDivisors(n):
    if n < 0: return 0

    res = []
    until = math.floor(math.sqrt(n))+1

    for i in range(1, until):
        if n % i == 0 :
            res.append(i)

        sec_divisor = n // i
        if sec_divisor != i:
            res.append(sec_divisor)

    res.sort()
    return res



# 4. Prime Number (following the above logic, to see divisors)

def isPrime(n):
    if n < 2 : return False
    max_range = math.floor(math.sqrt(n))

    for i in range(2, max_range+1):
        if n % i == 0:
            return False
    
    return True



#  5. Sieve Of Eratosthenes : Print number if it is prime in given range 'n'

# Brute Force : 
def brute_printPrime(n):
    res = []
    for i in range(n+1):
        if(isPrime(i)) : res.append(i)
    return res

# Optimized using Sieve algo :
def sieve_algo(n):
    res = [True] * (n+1)
    res[0] = False
    res[1] = False

    ans = []
    
    max_range = math.floor(math.sqrt(n))

    for i in range(2, max_range+1):
        for j in range(i*i, n+1, +i):
            res[j] = False
    
    for i,x in enumerate(res):
        if x: 
            ans.append(i)

    return ans



# 6. Greatest Common Divisor : (HCF) The greatest and common divisor between given 2 elements
    
def gcd(a,b):
    a,b= abs(a), abs(b)

    if a%b == 0 : return b
    if b%a == 0 : return a

    if a == 0 or b == 0 : return 0
    if a == 0 : return b
    if b == 0 : return a


    m_range = min(a,b) + 1
    greatest = 1
    
    for i in range(2, m_range ):
        if a%i == 0 and b%i == 0:
            greatest = max(greatest, i)
    
    return greatest

