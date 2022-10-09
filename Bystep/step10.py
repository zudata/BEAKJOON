# 10872
def fact(n):
    result = 1
    if n > 0 :
        result = n*fact(n-1)
    return result
n = int(input())
print(fact(n))

# 10870
def fibo(n):
    result = 1
    if n == 1: result = 1
    elif n > 1: result = fibo(n-1) + fibo(n-2)
    else: result = 0
    return result
n = int(input())
print(fibo(n))

# 25501
def recursion(s, l, r, c):
    c += 1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)
n = int(input())
for i in range(n):
    txt = input()
    print(isPalindrome(txt)[0], isPalindrome(txt)[1])