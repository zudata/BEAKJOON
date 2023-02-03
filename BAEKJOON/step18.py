# 11659
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
l = list(map(int, inputs().split()))
for _ in range(m):
    a, b = map(int, inputs().split())
    print(sum(l[a-1:b]))