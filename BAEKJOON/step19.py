# 11047
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
val = [int(inputs()) for _ in range(n)]
val.sort(reverse = True); res = 0
for i in val:
    if k//i > 0:
        res += k//i
        k = k%i
        if k == 0:
            print(res)
            break