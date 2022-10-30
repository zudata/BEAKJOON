# 5086
import sys
inputs = sys.stdin.readline
while True:
    a, b = map(int, inputs().split())
    if a == b == 0: break
    elif b%a == 0: print('factor')
    elif a%b == 0: print('multiple')
    else: print('neither')

# 1037
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
l.sort()
print(l[0]*l[n-1])

# 2609
import sys
inputs = sys.stdin.readline
a, b = map(int, inputs().split())
d = 2; res = 1
while a >= d and b >= d:
    if a%d == 0 and b%d == 0:
        a = a/d; b = b/d
        res = res*d
    else: d += 1
print(res)
print(int(res*a*b))

# 1934
import sys
inputs = sys.stdin.readline
def lc(x, y):
    r = x%y
    if r == 0: return y
    else: return lc(y, r)
for i in range(int(inputs())):
    a, b = map(int, inputs().split())
    l = lc(a, b)
    print((a//l)*(b//l)*l)