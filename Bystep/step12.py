# 10815
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = set(map(int, inputs().split()))
m = int(inputs())
ll = list(map(int, inputs().split()))
for i in ll:
    if i in l: print(1, end = ' ')
    else: print(0, end = ' ')