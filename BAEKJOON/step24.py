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