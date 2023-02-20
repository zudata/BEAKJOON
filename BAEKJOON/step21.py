# 18258
import sys
inputs = sys.stdin.readline
q = []; i = 0; n = int(inputs())
for _ in range(n):
    f = list(inputs().split())
    if len(f) == 2:
        q.append(f[1])
    else:
        if f[0] == 'pop':
            if len(q) <= i: print(-1)
            else:
                print(q[i])
                i += 1
        elif f[0] == 'size':
            print(len(q) - i)
        elif f[0] == 'empty':
            if len(q) - i == 0: print(1)
            else: print(0)
        elif f[0] == 'front':
            if len(q) - i == 0: print(-1)
            else: print(q[i])
        elif f[0] == 'back':
            if len(q) - i == 0: print(-1)
            else: print(q[-1])

# 2164
import sys
inputs = sys.stdin.readline
i = 1; n = int(inputs())
while n > i:
    i *= 2
print(n*2-i)

# 11866
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
num = [x for x in range(1, n+1)]; i = 0; res = []
while num:
    i += k - 1
    if i >= len(num):
        i = i % len(num)
    res.append(str(num.pop(i)))
    if num:
        res.append(', ')
print(f'<{"".join(res)}>')