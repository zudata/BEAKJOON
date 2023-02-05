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