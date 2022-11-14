# 15649
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
x = []
def seq():
    if len(x) == m:
        print(' '.join(map(str, x)))
        return
    for i in range(1, n+1):
        if i not in x:
            x.append(i)
            seq()
            x.pop()
seq()

# 15650
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
x = []; s = 1
def seq(s):
    if len(x) == m:
        print(' '.join(map(str, x)))
        return
    for i in range(s, n+1):
        if i not in x:
            x.append(i)
            s += 1
            seq(s)
            x.pop()
seq(s)

# 15651
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
x = []
def seq():
    if len(x) == m:
        print(' '.join(map(str, x)))
        return
    for i in range(1, n+1):
        x.append(i)
        seq()
        x.pop()
seq()

# 15652
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
x = []
def seq():
    if len(x) == m:
        print(' '.join(map(str, x)))
        return
    for i in range(1, n+1):
        if len(x) == 0 or x[-1] <= i:
            x.append(i)
            seq()
            x.pop()
seq()

# 9663
import sys
inputs = sys.stdin.readline
def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x]-arr[i]) == x-i:
            return 0
    return 1
def N_Queen(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                N_Queen(x + 1)
n = int(inputs())
arr = [0] * n; cnt = 0
N_Queen(0)
print(cnt)