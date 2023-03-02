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