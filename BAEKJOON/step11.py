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

# 24060
def merge_sort(l, p, r):
    if p < r and c <= k:
        q = (p+r)//2
        merge_sort(l, p , q)
        merge_sort(l, q+1, r)
        merge(l, p, q, r)
        
def merge(l, p, q, r):
    global c, res
    i = p; j = q+1
    tmp = []
    
    while i <= q and j <= r:
        if l[i] <= l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1
        
    while i <= q:
        tmp.append(l[i])
        i += 1
    
    while j <= r:
        tmp.append(l[j])
        j += 1
    
    i = p; t = 0
    
    while i <= r:
        l[i] = tmp[t]
        c += 1
        if c == k:
            res = l[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split())
l = list(map(int, input().split()))
c = 0
res = -1
merge_sort(l, 0, n - 1)
print(res)

# 2447
def star(n):
    if n == 3: return ['***', '* *', '***']
    arr = star(n//3)
    stars = []
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars
n = int(input())
print('\n'.join(star(n)))

# 11729
def hanoi(n, a, b, c):
    if n == 1: print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)
c = 1
n = int(input())
for i in range(n-1):
    c = c*2 + 1
print(c)
hanoi(n, 1, 2, 3)

# 27433
def fact(n):
    res = 1
    if n > 0 :
        res = n*fact(n-1)
    return res
print(fact(int(input())))

# 4779
import sys
inputs = sys.stdin.readline
def sol(n, i, j):
    if n == 0: return
    cnt = (j - i + 1) // 3
    sol(n - 1, i, i + cnt - 1)
    for k in range(i + cnt, i + cnt * 2): res[k] = ' '
    sol(n - 1, i + cnt * 2, i + cnt * 3 - 1)
while True:
    try:
        n = int(inputs())
        res = ['-'] * (3 ** n)
        sol(n, 0, 3 ** n - 1)
        print(''.join(res))
    except: break