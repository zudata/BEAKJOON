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

# 3053
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(3.14159265359*n**2)
print(2*n**2)

# 1002
import sys, math
inputs = sys.stdin.readline
t = int(inputs())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, inputs().split())
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    if dis == 0 and r1 == r2: print(-1)
    elif abs(r1-r2) < dis < r1+r2: print(2)
    elif math.isclose(r1+r2, dis) or math.isclose(abs(r1-r2), dis): print(1)
    else: print(0)
## 실수 비교 시에 == 사용하는 것은 위험 -> isclose로 비교하는 게 좋음

# 1004
import sys
inputs = sys.stdin.readline
t = int(inputs())
for i in range(t):
    x1, y1, x2, y2 = map(int, inputs().split())
    n = int(inputs())
    count = 0
    for i in range(n):
        cx, cy, r = map(int, inputs().split())
        d1 = ((x1-cx)**2 + (y1-cy)**2)**0.5
        d2 = ((x2-cx)**2 + (y2-cy)**2)**0.5
        if (d1 < r and d2 < r) or (d1 > r and d2 > r): pass
        else: count += 1
    print(count)

# 7785
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = set()
for _ in range(n):
    name, y = inputs().split()
    if y == 'enter': l.add(name)
    else: l.remove(name)
l = sorted(l, reverse = True)
print(*l, sep = '\n')