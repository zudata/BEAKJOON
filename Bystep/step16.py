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

# 2580
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
def check(x, y, n):
    for i in range(9):
        if board[x][i] == n or board[i][y] == n:
            return False
        if board[x//3*3 + i//3][y//3*3 + i%3] == n:
            return False
    return True
def sudoku(x, y):
    if x == 9:
        for row in board:
            print(' '.join(map(str, row)))
        exit(0)
    if board[x][y] != 0:
        if y == 8: sudoku(x+1, 0)
        else: sudoku(x, y+1)
    else:
        for i in range(1, 10):
            if check(x, y, i):
                board[x][y] = i
                if y == 8: sudoku(x+1, 0)
                else: sudoku(x, y+1)
            if i == 9:
                board[x][y] = 0
sudoku(0, 0)

# 14888
import sys
inputs = sys.stdin.readline
N = int(inputs())
A = list(map(int, inputs().split()))
Op = list(map(int, inputs().split()))

Min = 1e9
Max = -1e9

def Recur(Add, Sub, Mul, Div, n, Res):
    global Min,Max
    if n < N-1:
        if 0 < Add:
            Recur(Add-1, Sub, Mul, Div, n+1, Res+A[n+1])
        if 0 < Sub:
            Recur(Add, Sub-1, Mul, Div, n+1, Res-A[n+1])
        if 0 < Mul:
            Recur(Add, Sub, Mul-1, Div, n+1, Res*A[n+1])
        if 0 < Div:
            Recur(Add, Sub, Mul, Div-1, n+1, int(Res/A[n+1]))
    else:
        Min = min(Min,Res)
        Max = max(Max,Res)

Recur(Op[0], Op[1], Op[2], Op[3], 0, A[0])
print(Max)
print(Min)

# 14889
import sys
from math import factorial
inputs = sys.stdin.readline
N = int(inputs())
S = [list(map(int, inputs().split())) for _ in range(N)]
Team1 = []
Min = 100 * 400
Cnt = 0
End = factorial(N) // (factorial(N//2)**2)
def Recur(n,start):
    global Min, Cnt
    if n < N//2:
        for i in range(start,N):
            if i not in Team1:
                Team1.append(i)
                Recur(n+1,i+1)
                Team1.pop()
    else:
        Team2 = [i for i in range(N)]
        for i in Team1:
            Team2.remove(i)
        Sum1 = 0
        for i in range(N//2):
            for j in range(i,N//2):
                Sum1 += (S[Team1[i]][Team1[j]] + S[Team1[j]][Team1[i]])
        Sum2 = 0
        for i in range(N//2):
            for j in range(i,N//2):
                Sum2 += (S[Team2[i]][Team2[j]] + S[Team2[j]][Team2[i]])
        # print(Team1,Team2)
        Min = min(Min, abs(Sum1-Sum2))
        Cnt += 1
        if Cnt == End:
            print(Min)
            exit(0)

Recur(0,0)