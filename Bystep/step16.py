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