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
zero_pos = [(x,y) for x in range(9) for y in range(9) if board[x][y] == 0]
z_len = len(zero_pos)
offset = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, -1), (-1, 0), (0, 1), (0, -1), (0, 0)]
offset_pos = [1]*3+[4]*3+[7]*3
finished = False
def choice(x,y):
    nums = list(range(1,10))
    for n in range(9):
        if board[x][n] in nums:
            nums.remove(board[x][n])
        if board[n][y] in nums:
            nums.remove(board[n][y])
    for off in offset:
        dx = offset_pos[x]+off[0]
        dy = offset_pos[y]+off[1]
        if board[dx][dy] in nums:
            nums.remove(board[dx][dy])
    return nums

def dfs(cur):
    global finished
    if finished == True :
        return
    if cur == z_len:
        for item in board:
            print(*item)
        finished = True
        return
    else:
        (x,y) = zero_pos[cur]
        for c in choice(x,y):
            board[x][y] = c
            dfs(cur+1)
            board[x][y] = 0
dfs(0)