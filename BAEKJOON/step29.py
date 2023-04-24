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