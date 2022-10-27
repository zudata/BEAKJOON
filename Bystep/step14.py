# 1085
import sys
inputs = sys.stdin.readline
x, y, w, h = map(int, inputs().split())
l = [x, y, w-x, h-y]
print(min(l))

# 3009
import sys
inputs = sys.stdin.readline
x = []; y = []
for i in range(3):
    a, b = list(map(int, inputs().split()))
    if a not in x: x.append(a)
    else: x.remove(a)
    if b not in y: y.append(b)
    else: y.remove(b)
print(' '.join(str(j) for j in x+y))