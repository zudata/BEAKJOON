# 11654
print(ord(input()))

# 11720
n = int(input())
x = input()
p = 0
for i in x:
    p += int(i)
print(p)

# 10809
s = input()
a = 'abcdefghijklmnopqrstuvwxyz'
for i in a:
    print(s.find(i), end = ' ')

# 2675
t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    for j in s:
        print(j*int(r), end = '')
    print()

# 1157
s = input().upper()
p = []; res = {}
for i in range(len(s)):
    p.append(0)
d = dict(zip(s, p))
for i in s:
    d[i] += 1
m = max(d.values())
for k, v in d.items():
    if v == m: res[k] = v
if len(res) == 1:
    for k in res.keys(): print(k)
else: print('?')

# 1152
s = list(input().split())
print(len(s))

# 2908
a, b = map(str, input().split())
a = int(a[2]+a[1]+a[0])
b = int(b[2]+b[1]+b[0])
if a>b : print(a)
else: print(b)

# 5622
s = input()
a = 'ABCDEFGHIJKLMNOQRSTUVWXY'
t = 0
for i in s:
    if i == 'Z': t += 10
    elif i == 'P': t += 8
    else: t += (a.find(i)+3)//3+2
print(t)

# 2941
s = input()
ss = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in ss:
    s = s.replace(i, '*')
print(len(s))

# 1316
n = int(input())
c = 0
for i in range(n):
    s = input()
    d = 0; res = []
    for j in s:
        if j not in res:
            res.append(j)
            d += 1
        else:
            if res[len(res)-1] == j: d += 1
    if d == len(s): c += 1
print(c)

# 10798
import sys
inputs = sys.stdin.readline
s = [inputs().strip() for _ in range(5)]
res = []
for i in range(15):
    word = ''
    for j in range(5):
        try:
            word += s[j][i]
        except IndexError: pass
    res.append(word)
print(''.join(res))