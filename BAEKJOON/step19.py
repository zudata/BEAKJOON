# 11047
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
val = [int(inputs()) for _ in range(n)]
val.sort(reverse = True); res = 0
for i in val:
    if k//i > 0:
        res += k//i
        k = k%i
        if k == 0:
            print(res)
            break

# 1931
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = [list(map(int, inputs().split())) for _ in range(n)]
l.sort(key = lambda x : (x[1], x[0])); res = 1; m = l[0][1]
for i in l[1:]:
    if i[0] >= m:
        m = i[1]
        res += 1
print(res)

# 11399
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
l.sort()
res = l[0]; c = l[0]
for i in l[1:]:
    c += i
    res += c
print(res)

# 1541
import sys
inputs = sys.stdin.readline
s = inputs().strip().split('-')
plus = []
for ss in s:
    ss = ss.split('+')
    sums = 0
    for sss in ss:
        sums += int(sss)
    plus.append(sums)
res = plus[0]
for i in range(1, len(plus)):
    res -= plus[i]
print(res)