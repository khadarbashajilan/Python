# FizzBuzz – Print numbers 1–100; multiples of 3 → “Fizz”, 5 → “Buzz”, 15 → “FizzBuzz”.

def fizzbuzz(n)  :
    ans = []
    for i in range(1,n+1):
        if i %3 ==0 and i%5 ==0:
            ans.append("FizzBuzz")
        elif i%3 ==0:
            ans.append("Fizz")
        elif i%5 ==0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans

print(fizzbuzz(15))

# Palindrome Number – Check if a given integer is a palindrome.

def pali(n):
    rev = 0
    x = n
    while x > 0:
        ld = x % 10
        rev = rev * 10 + ld
        x = x//10
    return rev == n

print(pali(1223221))


#Count Digits – Count number of digits in an integer.

def count_dig(n):
    count = 0
    while n>0:
        count += 1
        n= n//10
    return count


print(count_dig(12345689))

#Sum of Natural Numbers – Input n, output sum 1+2+...+n.

def sum_all(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

print(sum_all(123))

#Reverse Integer – Reverse the digits of a number.

def reverse_int(n):
    sign = 1 if n > 0 else -1
    n = abs(n)
    x = n
    rev = 0
    while x>0 :
        ld = x%10
        rev = rev*10 + ld
        x = x//10
    return rev * sign

print(reverse_int(-123456))


