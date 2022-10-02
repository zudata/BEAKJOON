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

# 10989
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = [0 for i in range(10001)]
for i in range(n):
    l[int(inputs())] += 1
for j in range(1, 10001):
    if l[j] != 0:
        for k in range(l[j]):
            print(j)

# 25305
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(l[n-k])
