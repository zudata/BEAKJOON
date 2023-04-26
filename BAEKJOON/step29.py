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