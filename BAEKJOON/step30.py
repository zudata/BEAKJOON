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

# 24480
import sys
inputs = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1); tmp = 1
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph:
    i.sort(reverse = True)
def algorithm(v):
    global tmp
    res[v] = tmp
    for i in graph[v]:
        if res[i]: continue
        tmp += 1
        algorithm(i)
algorithm(r)
print(*res[1:], sep = '\n')

# 24444
import sys
from collections import deque
inputs = sys.stdin.readline
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph: 
    i.sort()
def algorithm(v):
    cnt = 1
    queue = deque([v])
    res[v] = cnt 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if res[i] == 0:
                cnt += 1
                queue.append(i)
                res[i] = cnt 
algorithm(r)
print(*res[1:], sep = '\n')

# 24445
import sys
from collections import deque
inputs = sys.stdin.readline
n, m, r = map(int, inputs().split())
graph = [[] for _ in range(n+1)]
res = [0]*(n+1)
for _ in range(m):
    u, v = map(int, inputs().split())
    graph[u].append(v); graph[v].append(u)
for i in graph: 
    i.sort(reverse = True)
def algorithm(v):
    cnt = 1
    queue = deque([v])
    res[v] = cnt 
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if res[i] == 0:
                cnt += 1
                queue.append(i)
                res[i] = cnt 
algorithm(r)
print(*res[1:], sep = '\n')