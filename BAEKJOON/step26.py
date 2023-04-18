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