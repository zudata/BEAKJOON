# 2738
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
res = []
for i in range(n):
    res.append(list(map(int, inputs().split())))
for j in range(n):
    l = list(map(int, inputs().split()))
    for k in range(m):
        res[j][k] += l[k]
    print(' '.join(str(r) for r in res[j]))

# 2566
import sys
inputs = sys.stdin.readline
m = -1
for i in range(9):
    l = list(map(int, inputs().split()))
    max_value = max(l)
    if m < max_value:
        m = max_value
        r = i+1; c = l.index(max_value)+1
print(m)
print(r, c)

# 2563
import sys
inputs = sys.stdin.readline
n = int(inputs())
boxs = set()
for i in range(n):
    x, y = map(int, inputs().split())
    for j in range(10):
        for k in range(10):
            boxs.add((x+j, y+k))
print(len(boxs))

# 2743
import sys
inputs = sys.stdin.readline
s = inputs().strip()
print(len(s))

# 9086
import sys
inputs = sys.stdin.readline
t = int(inputs())
for _ in range(t):
    s = inputs().strip()
    print(f'{s[0]}{s[-1]}')

# 11718
while True:
    try:
        print(input())
    except EOFError:
        break