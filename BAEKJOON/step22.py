# 1966
import sys
inputs = sys.stdin.readline
t = int(inputs())
for _ in range(t):
    n, m = map(int, inputs().split())
    ip = list(map(int, inputs().split()))
    id = list(range(n))
    res = 0; id[m] = -1
    while True:
        if ip[0] == max(ip):
            res += 1
            if id[0] == -1:
                print(res)
                break
            else:
                ip.pop(0); id.pop(0)
        else:
            ip.append(ip.pop(0))
            id.append(id.pop(0))

# 10866
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = []
for _ in range(n):
    m = list(map(str, inputs().split()))
    if m[0] == 'push_front':
        l = [m[1]] + l
    elif m[0] == 'push_back':
        l += [m[1]]
    elif m[0] == 'pop_front':
        try:
            print(l[0])
            l = l[1:]
        except: print(-1)
    elif m[0] == 'pop_back':
        try:
            print(l[-1])
            l = l[:-1]
        except: print(-1)
    elif m[0] == 'size':
        print(len(l))
    elif m[0] == 'empty':
        if len(l) == 0: print(1)
        else: print(0)
    elif m[0] == 'front':
        try:
            print(l[0])
        except: print(-1)
    else:
        try:
            print(l[-1])
        except: print(-1)