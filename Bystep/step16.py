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
n = int(inputs())
res = 0
def queen(x, s):
    global res
    if len(s) == n:
        res += 1
        return
    for y in range(n):
        check = True
        for r, c in s:
            if y == c or abs(x-r) == abs(y-c):
                check = False
                break
        if check:
            s.append((x, y))
            queen(x+1, s)
            s.pop()
queen(0, [])
print(res)