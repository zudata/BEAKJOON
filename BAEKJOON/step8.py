# 1712
a, b, c = map(int, input().split())
if c-b == 0 or b-c > 0: print(-1)
else: print(int(a/(c-b))+1)

# 2292
n = int(input())
r = 1; c = 1
while n > c:
    c += r*6
    r += 1
print(r)

# 1193
n = int(input())
l = 0; c = 0
while n > l:
    c += 1
    l += c
a = l - n
if c % 2 == 0: print(f'{(c-a)}/{(a+1)}')
else: print(f'{a+1}/{(c-a)}')

# 2869
a, b, v = map(int, input().split())
d = (v-a)/(a-b)
if d > int(d): print(int(d)+2)
else: print(int(d)+1)

# 10250
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    a = n%h
    if a == 0: a = h; b = n//h
    else: b = n//h+1
    print(f'{a}{b:0>2}')

# 2775
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    l = [[0 for col in range(n+1)] for row in range(k+1)]
    for i in range(1, n+1):
        l[0][i] = i
    for j in range(k+1):
        l[k][1] = 1
    for i in range(1, k+1):
        for j in range(1, n+1):
            l[i][j] = (l[i-1][j] + l[i][j-1])
    print(l[k][n])

# 2839
n = int(input())
11
a = n//5
while a >= 0:
    b = (n-(a*5))//3
    m = (n-(a*5))%3
    if m == 0: break
    a -= 1
if a < 0: print(-1)
else: print(a+b)

# 10757
import sys; inputs = sys.stdin.readline
a, b = map(int, inputs().split())
print(a+b)