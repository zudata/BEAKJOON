# 10815
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = set(map(int, inputs().split()))
m = int(inputs())
ll = list(map(int, inputs().split()))
for i in ll:
    if i in l: print(1, end = ' ')
    else: print(0, end = ' ')

# 14425
n, m = map(int, input().split())
ll = []; l = set(); count = 0
for i in range(n):
    l.add(input())
for j in range(m):
    ll.append(input())
for k in ll:
    if k in l: count += 1
print(count)