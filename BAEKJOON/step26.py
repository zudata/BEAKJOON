# 11066
import sys
inputs = sys.stdin.readline
for _ in range(int(inputs())):
    k = int(inputs())
    chapters = list(map(int, inputs().split()))
    arr = [[0 for __ in range(k)] for ___ in range(k)]
    for gap in range(1, k):
        for start in range(k):
            end = start + gap
            if end >= k: break
            arr[start][end] = 9999999999
            tmp = sum(chapters[start:end+1])
            for i in range(start, end):
                arr[start][end] = min(arr[start][end], arr[start][i] + arr[i+1][end] + tmp)
    print(arr[0][k-1])

# 11049
import sys
inputs = sys.stdin.readline
n = int(inputs())
arr = [list(map(int, inputs().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(n-i) :
        if i == 1: dp[j][j+1] = arr[j][0]*arr[j][1]*arr[j+1][1]
        else :
            dp[j][j+i] = 2**31
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1]) 
print(dp[0][n-1])

# 1520
import sys
inputs = sys.stdin.readline
m, n = map(int, inputs().split())
arr = [list(map(int, inputs().split())) for _ in range(m)]
route=[[-1]*n for _ in range(m)]
dx=[1,-1,0,0]; dy=[0,0,1,-1]
def dfs(start):
    x, y = start
    if x == m-1 and y == n-1: return 1
    if route[x][y] != -1: return route[x][y]
    route[x][y] = 0
    for i in range(4):
        xx = x + dx[i]; yy = y + dy[i]
        if xx < 0 or xx >= m or yy < 0 or yy >= n: continue
        if arr[xx][yy] < arr[x][y]: route[x][y] += dfs([xx,yy])
    return route[x][y]
dfs([0,0])
print(route[0][0])

# 2629
import sys
inputs = sys.stdin.readline
n = int(inputs())
l1 = list(map(int, inputs().split()))
m = int(inputs())
l2 = list(map(int, inputs().split()))
arr = [[0 for _ in range(15001)] for _ in range(n+1)]; res = []
def weight(x, y, i):
    global n, l1, arr, res
    d = abs(x - y)
    if d not in res:
        res.append(d)
    if i == n:
        return 0
    if arr[i][d] == 0:
        weight(x + l1[i], y, i+1)
        weight(x, y + l1[i], i+1)
        weight(x, y, i+1)
        arr[i][d] = 1
weight(0, 0, 0)
for i in range(m):
    if l2[i] in res: print('Y', end=' ')
    else: print('N', end=' ')

# 2293
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
l = [int(inputs()) for _ in range(n)]
dp = [1] + [0]*(k)
for i in l:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[k])