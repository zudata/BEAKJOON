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
dp = [0]*1000001
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n])

# 9461
import sys
inputs = sys.stdin.readline
dp = [0]*101
def p(x):
    if dp[x] != 0: return dp[x]
    if x == 1 or x == 2 or x == 3: return 1
    dp[x] = p(x-2) + p(x-3)
    return dp[x]
for i in range(int(inputs())):
    n = int(inputs())
    print(p(n))

# 1912
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
dp = [0]*n
dp[0] = l[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + l[i], l[i])
print(max(dp))

# 1149
import sys
inputs = sys.stdin.readline
n = int(inputs())
dp = []
for _ in range(n):
    dp.append(list(map(int, inputs().split())))
for i in range(1, n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))

# 1932
import sys
inputs = sys.stdin.readline
dp = []
for _ in range(int(inputs())):
    dp.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, len(dp)):
    dp[i][0] += dp[i-1][0]
    dp[i][-1] += dp[i-1][-1]
    if i >= 2:
        for j in range(1, i):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))

# 2579
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = []
for _ in range(n): l.append(int(inputs()))
dp = [l[0]]
for i in range(1, n):
    if i == 1: dp.append(max(l[i] + dp[i-1], l[i]))
    elif i == 2: dp.append(max(l[i] + l[i-1], l[i] + dp[i-2]))
    else: break
for i in range(3, n):
    dp.append(max(l[i] + l[i-1] + dp[i-3], l[i] + dp[i-2]))
print(dp[-1])