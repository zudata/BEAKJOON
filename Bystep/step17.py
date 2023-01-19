# 24416
import sys
inputs = sys.stdin.readline
n = int(inputs())
ans1 = 0
def fibo1(n):
    global ans1
    if n == 1 or n == 2:
        ans1 += 1
        return 1
    else: return fibo1(n-1) + fibo1(n-2)
def fibo2(n):
    ans2 = 0
    fib = [1]*n
    for i in range(2, n):
        ans2 += 1
        fib[i] = fib[i-2] + fib[i-1]
    return ans2
fibo1(n)
print(ans1, fibo2(n))

# 9184
import sys
inputs = sys.stdin.readline
w_dic = {} # 이미 했던 경로 저장함으로써 시간 단축
def w(a, b, c):
    if (a, b, c) in w_dic:
        return w_dic[(a, b, c)]
    elif a <= 0 or b <= 0 or c <= 0:
        w_dic[(a, b, c)] = 1
        return w_dic[(a, b, c)]
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        w_dic[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w_dic[(a, b, c)]
    else:
        w_dic[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return w_dic[(a, b, c)]

while True:
    a, b, c = map(int, inputs().split())
    if a == -1 and b == -1 and c == -1: break
    else:
        ans = w(a, b, c)
        print(f'w({a}, {b}, {c}) = {ans}')

# 1904
import sys
inputs = sys.stdin.readline
n = int(inputs())
r = n//2; res = 0
def c(n, r):
    com = 1
    for x in range(n, n-r, -1):
        com *= x
    for y in range(2, r+1):
        com /= y
    return com
for i in range(r+1):
    res += c(n, i)
    n -= 1
print(int(res%15746))