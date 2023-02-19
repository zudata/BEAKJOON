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
