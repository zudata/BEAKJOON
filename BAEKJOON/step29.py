# 9935
import sys
inputs = sys.stdin.readline
s = list(inputs().strip())
bomb = inputs().strip()
res = []
for i in range(len(s)):
    res.append(s[i])
    if ''.join(res[-len(bomb):]) == bomb:
        for i in range(len(bomb)): res.pop()
if res: print(''.join(res))
else: print('FRULA')

# 17298
import sys
inputs = sys.stdin.readline
n = int(inputs())
a = list(map(int, inputs().split()))
res = [-1]*n; stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        res[stack.pop()] = a[i]
    stack.append(i)
print(*res)

# 17299
import sys
import collections
inputs = sys.stdin.readline
n = int(inputs())
a = list(map(int, inputs().split()))
cnt = collections.Counter(a)
res = [-1]*n; stack = [0]
for i in range(1, n):
    while stack and cnt[a[stack[-1]]] < cnt[a[i]]:
        res[stack.pop()] = a[i]
    stack.append(i)
print(*res)

# 1725
import sys
inputs = sys.stdin.readline
n = int(inputs())
res = 0; graph = [int(inputs()) for _ in range(n)] + [0]
stack = [(0, graph[0])]
for i in range(1, n+1):
    x = i
    while stack and stack[-1][1] > graph[i]:
        x, h = stack.pop()
        res = max(res, (i - x) * h)
    stack.append((x, graph[i]))
print(res)

# 3015
import sys
inputs = sys.stdin.readline
n = int(inputs())
res = 0; stack = []
for _ in range(n):
    h = int(inputs())
    while stack and stack[-1][0] < h: res += stack.pop()[1]
    if stack and stack[-1][0] == h:
        cnt = stack.pop()[1]
        res += cnt
        if len(stack) != 0:
            res += 1
        stack.append((h, cnt + 1))
    else:
        if len(stack) != 0: res += 1
        stack.append((h, 1))
print(res)