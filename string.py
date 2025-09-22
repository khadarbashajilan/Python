# Valid Palindrome (LeetCode #125).

def valid_pali(s):
    x = ""
    for i in s:
        if i.isalpha() or i.isalnum():
            x += i.lower()
    # return x == x[::-1]
    st = 0
    end = len(x)-1
    while st<=end:
        if x[st] == x[end]:
            st += 1
            end -= 1
        else:
            return False
    return True

print(valid_pali("A man, a plan, a canal: Panama"))


#Reverse String – (LeetCode #344).

def reverse_s(s):
    st = 0
    end = len(s)-1
    while st<=end:
        s[st],s[end]=s[end], s[st]
        st += 1
        end -= 1
    print(s)

reverse_s(["h","e","l","l","o"])


#First Unique Character in a String (LeetCode #387).

s = "loveleetcode"

def Uniq_ch(s):
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0)+1
    
    for i, ch in enumerate(s):
        if d[ch] == 1:
            return i
    return -1

print(Uniq_ch(s))


#Implement strStr() – (LeetCode #28).

def strStr(haystack, needle) :
        return -1 if needle not in haystack else haystack.index(needle)

print(strStr("sadbutsad", "sad"))


#Valid Anagram LC#242

def valid_ana(s,t):
    # 0(n)
    dic1 = {}
    dic2 = {}
    for i in s:
        dic1[i] = dic1.get(i, 0)+1
    for i in t:
        dic2[i] = dic2.get(i, 0) + 1
    return dic1 == dic2

    # 0(nlogn):
    # s2 = list(t)
    # s1 = list(s)
    # print(s1 == s2)
    # s1 = sorted(s1)
    # s2 = sorted(s2)
    # return s1 == s2

print(valid_ana("anagram", "nagaram"))


