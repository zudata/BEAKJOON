# 15596
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return(ans)

# 4673
s = set(range(1, 10001))
for n in range(1, 10001):
    for i in str(n):
        n += int(i)
    s.discard(n)
for j in s:
    print(j)

# 1065
n = int(input())
if n < 100: count = n
else:
    count = 99
    for i in range(100, n+1):
        string = []
        for j in str(i):
            string.append(j)
        if int(string[1])*2 == int(string[0]) + int(string[2]): count += 1
print(count)

# 2444
import sys
inputs = sys.stdin.readline
n = int(inputs())
for i in range(n):
    print(f'{" "*(n-i-1)}{"*"*(2*(i+1)-1)}')
for i in range(n-2, -1, -1):
    print(f'{" "*(n-i-1)}{"*"*(2*(i+1)-1)}')

# 10812
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
b = [str(x+1) for x in range(n)]
for _ in range(m):
    i, j, k = map(int, inputs().split())
    eb = b[k-1:j]+b[i-1:k-1]
    b[i-1:j] = eb
print(' '.join(b))

# 10988
import sys
inputs = sys.stdin.readline
s = inputs().strip()
n = len(s); test = [s[i] for i in range(-1, -(n+1)//2, -1)]
if s[:n//2] == ''.join(test): print(1)
else: print(0)

# 25206
import sys
inputs = sys.stdin.readline
d = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
s = 0; c = 0
for _ in range(20):
    i, j, k = inputs().split()
    if k == 'P': pass
    else:
        c += float(j)
        s += d[k]*float(j)
print(s/c)