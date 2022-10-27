# 1085
import sys
inputs = sys.stdin.readline
x, y, w, h = map(int, inputs().split())
l = [x, y, w-x, h-y]
print(min(l))

