# 2750
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
for j in range(n):
    print(l[j])

# 2751
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = []
for i in range(n):
    l.append(int(inputs()))
l.sort()
for j in range(n):
    print(l[j])
