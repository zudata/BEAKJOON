# 1920
import sys
inputs = sys.stdin.readline
n = int(inputs())
nl = set(map(int, inputs().split()))
m = int(inputs())
ml = list(map(int, inputs().split()))
for i in ml:
    if i in nl: print(1)
    else: print(0)

# 1654
import sys
inputs = sys.stdin.readline
k, n = map(int, inputs().split())
l = [int(inputs()) for _ in range(k)]
t = 1; res = max(l)
while t <= res:
    mid = (t + res) // 2
    ln = 0
    for i in l: ln += i // mid
    if ln >= n: t = mid + 1
    else: res = mid - 1
print(res)

# 2805
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
b = list(map(int, inputs().split()))
t, res = 1, max(b)
while t <= res:
    mid = (t + res) // 2
    ln = 0
    for i in b:
        if i >= mid: ln += i - mid
    if ln >= m: t = mid + 1
    else: res = mid - 1
print(res)