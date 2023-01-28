# 2739
n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n*i)

# 10950
t = int(input())
for tt in range(t):
    a, b = map(int, input().split())
    print(a + b)

# 8393
n = int(input())
for i in range(n):
    n += i
print(n)

# 25304
x = int(input())
n = int(input())
y = 0

for i in range(n):
    a, b = map(int, input().split())
    y += a*b
if x == y: print('Yes')
else: print('No')

# 15552
import sys
inputs = sys.stdin.readline
t = int(inputs())
for i in range(t):
    a, b = map(int, inputs().split())
    print(a + b)

# 11021
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')

# 11022
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')

# 2438
t = int(input())
for i in range(t):
    print('*' * (i+1))

# 2439
n = int(input())
for i in range(0, n):
    print(' ' * (n-1-i) + '*' * (i+1))

# 10871
n, x = map(int, input().split())
nn = list(map(int, input().split()))
for i in range(n):
    if nn[i] < x: print(nn[i], end = ' ')

# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    print(a+b)

# 10951
while True:
    try: a, b = map(int, input().split())
    except: break
    print(a+b)

# 1110
n = int(input())
nn = n
count = 0

while True:
    nn = (nn % 10) * 10 + (nn // 10 + nn % 10) % 10
    count += 1
    if n == nn: break
print(count)