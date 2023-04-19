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