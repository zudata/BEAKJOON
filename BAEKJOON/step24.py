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

# 2110
import sys
inputs = sys.stdin.readline
n, c = map(int, inputs().split())
l = sorted([int(inputs()) for _ in range(n)])
start = 1; end = l[n-1] - l[0]
while start <= end:
    cnt = 1; cur = l[0]
    mid = (start + end) // 2
    for i in l:
        if cur + mid <= i:
            cnt += 1; cur = i
    if cnt >= c:
        start = mid + 1; res = mid
    else: end = mid - 1
print(res)

# 1300
import sys
inputs = sys.stdin.readline
n = int(inputs()); k = int(inputs())
start = 1; end = k
while start <= end:
    mid = (start + end) // 2; cnt = 0
    for i in range(1,n+1): cnt += min(n, mid//i)
    if cnt >= k:
        res = mid; end = mid-1
    else: start = mid+1
print(res)