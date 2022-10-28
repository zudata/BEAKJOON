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

# 4153
import sys
inputs = sys.stdin.readline
while True:
    l = list(map(int, inputs().split()))
    l.sort()
    if l == [0, 0, 0]: break
    elif l[0]**2 + l[1]**2 == l[2]**2: print('right')
    else: print('wrong')

# 2477
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = []; w = 0; h = 0; indw = 0; indh = 0
for i in range(6):
    l.append(list(map(int, inputs().split())))
for v, x in enumerate(l):
    if x[0] > 2 and x[1] > w:
        w = x[1]; indw = v
    elif x[0] < 3 and x[1] > h:
        h = x[1]; indh = v
print(n*(w*h - l[(indw+3)%6][1]*l[(indh+3)%6][1]))