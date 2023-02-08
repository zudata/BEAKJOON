# 11659
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
l = list(map(int, inputs().split()))
tmp = 0; res=[0]
for i in l:
    tmp += i
    res.append(tmp)
for i in range(m):
    a, b = map(int,inputs().split())
    print(res[b]-res[a-1])

# 2559
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
l = list(map(int, inputs().split()))
s = sum(l[:k]); res = s
for i in range(n-k):
    s = s + l[i+k] - l[i]
    if (res < s): res = s
print(res)

# 16139
import sys
inputs = sys.stdin.readline
s = inputs().strip()
q = int(inputs())
arr = [[0]*26 for i in range(len(s))]
arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    arr[i][ord(s[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
for i in range(q):
    a, l, r = inputs().split(); l = int(l); r = int(r)
    orda = ord(a) - 97
    if l > 0:
        res = arr[r][orda] - arr[l - 1][orda]
    else:
        res = arr[r][orda]
    print(res)

# 10986
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
a = list(map(int, inputs().split())) + [0]
r = [0]*m
for i in range(n):
    a[i] += a[i-1]
    r[a[i]%m] += 1
res = r[0]
for i in r: res += i*(i-1)//2
print(res)

# 11660
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
l = [list(map(int, inputs().split())) for _ in range(n)]
sums = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
    for j in range(n):
        sums[i+1][j+1] = sums[i+1][j] + sums[i][j+1] - sums[i][j] + l[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, inputs().split())
    print(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1])

# 25682
import sys
inputs = sys.stdin.readline
n, m, k = map(int, inputs().split())
board = [list(inputs().rstrip()) for _ in range(n)]
def mini(col):
    sums = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0: 
                val = board[i][j] != col
            else:
                val = board[i][j] == col
            sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] - sums[i][j] + val
    count = int(1e9)
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, sums[i+k-1][j+k-1] - sums[i+k-1][j-1] - sums[i-1][j+k-1] + sums[i-1][j-1])
    return count
print(min(mini('B'), mini('W')))