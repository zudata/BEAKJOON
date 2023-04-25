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