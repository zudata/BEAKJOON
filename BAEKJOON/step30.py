# 24479
import sys
inputs = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]; path = []; res = [0]*(n+1); tmp = [-1]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in range(1, len(graph)):
    graph[i].sort()
def algorithm(x):
    tmp[x] = 1
    path.append(x)
    for i in graph[x]:
        if tmp[i] == -1: algorithm(i)
    return
algorithm(r)
for idx, node in zip(range(1, len(path)+1), path):
    res[node] = idx
print(*res[1:], sep = '\n')