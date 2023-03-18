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

# 1629
import sys
inputs = sys.stdin.readline
a, b, c = map(int, inputs().split())
def mul(a, b, c):
    if b == 1: return a%c
    m = mul(a, b//2, c)
    if not b%2: return (m*m)%c
    else: return (m*m*a)%c
print(mul(a, b, c))

# 11401
import sys
inputs = sys.stdin.readline
p = 1000000007
n, k = map(int, inputs().split())
def fact(num, mod):
    res = 1
    for i in range(2, num+1):
        res = res * i % p
    return res
def pow(num, p, mod):
    if p == 1: return num % mod
    if p % 2: return ((pow(num,p//2,mod) ** 2) * num) % mod
    else: return (pow(num,p//2,mod) ** 2) % mod
print(fact(n, p) * pow((fact(k, p) * fact(n-k, p)), p-2, p) % p)

# 2740
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
a = [list(map(int, inputs().split())) for _ in range(n)]
m, k = map(int, inputs().split())
b = [list(map(int, inputs().split())) for _ in range(m)]
for i in range(n):
    res = []
    for j in range(k):
        x = 0
        for l in range(m):
            x += a[i][l]*b[l][j]
        res.append(x)
    print(*res)

# 10830
import sys
inputs = sys.stdin.readline
def mul(n, mat1, mat2):
    res = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k]*mat2[k][j]
            res[i][j] %= 1000
    return res
def div(n, b, mat):
    if b == 1: return mat
    elif b == 2: return mul(n, mat, mat)
    else:
        tmp = div(n, b//2, mat)
        if b%2 == 0: return mul(n, tmp, tmp)
        else: return mul(n, mul(n, tmp, tmp), mat)
n, b = map(int, inputs().split())
arr = [list(map(int, inputs().split())) for _ in range(n)]
res = div(n, b, arr)
for i in res:
    for j in i:
        print(j%1000, end = ' ')
    print()