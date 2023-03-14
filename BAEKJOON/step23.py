# 2630
import sys
inputs = sys.stdin.readline
n = int(inputs())
arr = [list(map(int, inputs().split())) for _ in range(n)]
c1 = 0; c2 = 0
def square(x, y, n):
    global c1, c2
    col = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if col != arr[i][j]:
                n //= 2
                square(x, y, n)
                square(x+n, y, n)
                square(x, y+n, n)
                square(x+n, y+n, n)
                return
    if col == 0: c1 += 1
    else: c2 += 1
    return
square(0, 0, n)
print(c1, c2, sep = '\n')

# 1992
import sys
inputs = sys.stdin.readline
n = int(inputs())
arr = [inputs() for _ in range(n)]
def paper(x, y, n):
    n //= 2
    if n == 0:
        return arr[x][y]
    q1 = paper(x, y, n)
    q2 = paper(x, y+n, n)
    q3 = paper(x+n, y, n)
    q4 = paper(x+n, y+n, n)
    if (q1 in ['0', '1']) and q1 == q2 == q3 == q4:
        return q1
    return '(' + q1 + q2 + q3 + q4 + ')'
print(paper(0, 0, n))

# 1780
import sys
inputs = sys.stdin.readline
n = int(inputs())
arr = [list(map(int, inputs().split())) for _ in range(n)]
res1, res2, res3 = 0, 0, 0
def check(x, y, n):
    global res1, res2, res3
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num :
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3, y+l*n//3, n//3)
                return
    if num == -1: res1 += 1
    elif num == 0: res2 += 1
    else: res3 += 1
check(0, 0, n)
print(res1, res2, res3, sep = '\n')