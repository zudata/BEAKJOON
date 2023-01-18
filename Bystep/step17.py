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
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while True:
    a, b, c = map(int, inputs().split())
    if a == -1 and b == -1 and c == -1: break
    else:
        ans = w(a, b, c)
        print(f'w({a}, {b}, {c}) = {ans}')