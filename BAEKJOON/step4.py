# 10818
n = int(input())
x = list(map(int, input().split()))
print(min(x), max(x))

# 2562
x = []
for i in range(9):
    x.append(int(input()))
print(max(x))
print(x.index(max(x))+1)

# 3052
x = []
for i in range(10):
    x.append(int(input())%42)
print(len(set(x)))

# 1546
n = int(input())
p = list(map(int, input().split()))
mx = max(p)
for i in range(n):
    p[i] = p[i]/mx*100
print(sum(p)/n)

# 8958
n = int(input())
for i in range(n):
    a = input()
    p = 0
    count = 0
    for j in range(len(a)):
        if a[j] == 'O': 
            count += 1
            p += count
        else: count = 0
    print(p)

# 4344
c = int(input())
for i in range(c):
    s = list(map(int, input().split()))
    n = s[0]
    s.pop(0)
    mean = sum(s)/n
    count = 0
    for j in range(n):
        if s[j] > mean: count += 1
    print(f'{count/n*100:.03f}%')

# 10807
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
print(l.count(int(inputs())))

# 5597
l = {i for i in range(1, 31)}
for j in range(28):
    l.remove(int(input()))
for k in list(l):
    print(k)

# 10810
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
b = ['0' for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, inputs().split())
    for x in range(i -1, j):
        b[x] = str(k)
print(" ".join(b))