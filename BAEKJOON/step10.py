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

# 2108
import sys
inputs = sys.stdin.readline
n = int(inputs())
c = [0]*8001; l = []; ll = []
for i in range(n):
    m = int(inputs())
    c[4000+m] += 1
    l.append(m)
for j in range(8001): #최빈값
    if c[j] == max(c): ll.append(j - 4000)
if len(ll) == 1: a3 = ll[0]
else:
    ll.remove(min(ll))
    a3 = min(ll)
a1 = round(sum(l)/n) #산술평균
a4 = max(l) - min(l) #범위
l.sort()
a2 = l[int(n/2)] #중앙값
print(a1)
print(a2)
print(a3)
print(a4)

# 1427
import sys
inputs = sys.stdin.readline
n = list(map(int,inputs()))
n.sort(reverse = True)
for i in n:
    print(i, end='')

# 11650
import sys
inputs = sys.stdin.readline
l = []
n = int(inputs())
for i in range(n):
    (x, y) = map(int, inputs().split())
    l.append((x, y))
l.sort()
for j in l:
    print(j[0], j[1])

# 11651
import sys
inputs = sys.stdin.readline
l = []
n = int(inputs())
for i in range(n):
    (x, y) = map(int, inputs().split())
    l.append((y, x))
l.sort()
for j in l:
    print(j[1], j[0])

# 1181
l = []
n = int(input())
for i in range(n):
    word = input()
    l.append((len(word), word))
l = list(set(l))
l.sort()
for j in l:
    print(j[1])

# 10814
l = []
n = int(input())
for i in range(n):
    num, word = input().split()
    l.append((int(num), i, word))
l.sort()
for j in l:
    print(j[0], j[2])

# 18870
import sys
inputs = sys.stdin.readline
n = int(inputs())
x = list(map(int, inputs().split()))
l = list(set(x))
l.sort()
dict = {l[i]:i for i in range(len(l))}
for j in x:
    print(dict[j], end=' ')

# 2587
import sys
inputs = sys.stdin.readline
l = []
for i in range(5):
    l.append(int(inputs()))
l.sort()
print(int(sum(l)/5))
print(l[2])