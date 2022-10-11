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

# 24060 ?????
def merge_sort(l, p, r):
    if p < r:
        q = (p+r)//2 # q는 p, r의 중간 지점
        merge_sort(l, p, q) # 전반부 정렬
        merge_sort(l, q+1, r) # 후반부 정렬
        merge(l, p, q, r) # 병합
def merge(l, p, q, r):
    global c
    i = p; j = q; t = 1; tmp = []
    while i <= q and j <= r:
        if l[i] <= l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(l[i])
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(l[j])
        i = p; t = 0
    while i <= r:  # 결과를 A[p..r]에 저장
        l[i] = tmp[t]
        c += 1
        if c == k:
            print(l[i])
            sys.exit()
        i += 1; t += 1

n, k = map(int, input().split())
l = list(map(int, input().split()))
merge_sort(l, 0, n-1)

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