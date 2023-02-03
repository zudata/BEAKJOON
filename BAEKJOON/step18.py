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