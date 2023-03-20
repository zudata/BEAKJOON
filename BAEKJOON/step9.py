# 1978
n = int(input())
l = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    if l[i] == 1: l.remove(1)
    for j in range(2, l[i]):
        if l[i]%j == 0: l.remove(l[i]); break
print(len(l))

# 2581
m = int(input())
n = int(input())
l = [i for i in range(m, n+1)]
k = []
for i in range(len(l)):
    if l[i] == 1: k.append(l[i])
    for j in range(2, l[i]):
        if l[i]%j == 0: k.append(l[i]); break
for kk in k:
    l.remove(kk)
if len(l) == 0: print(-1)
else: print(sum(l)); print(min(l))

# 11653
n = int(input())
ii = []
i = 2
while i <= n:
    if n%i == 0:
        n = n/i
        ii.append(i)
    else: i += 1
for iii in ii:
    print(iii)

# 1929
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
m, n = map(int, input().split())
for j in range(m, n+1):
    if isPrime(j): print(j)

# 4948
def isPrime(num):
    if num==1:
        return 0
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return 0
        return 1
k = 123456*2+1
l = [1]*k
for i in range(k):
    l[i-1] = isPrime(i)

while True:
    n = int(input())
    count = 0
    if n == 0: break
    for i in range(n+1, 2*n+1):
        count += l[i-1]
    print(count)

# 9020
def isPrime(num):
    if num==1:
        return 0
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return 0
        return 1
l = []
for i in range(10000):
    if isPrime(i): l.append(i)

t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        for j in range(2*n):
            if (n/2+j in l) and (n/2-j in l): print(int(n/2-j), int(n/2+j)); break
    else:
        for j in range(2*n):
            if ((n-1)/2+j+1 in l) and ((n-1)/2-j in l):
                print(int((n-1)/2-j), int((n-1)/2+j+1)); break
            elif ((n-1)/2+j in l) and ((n-1)/2-j+1 in l):
                print(int((n-1)/2-j+1), int((n-1)/2+j)); break

# 2501
import sys
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
res = set()
for i in range(1, n//2):
    if n%i == 0:
        res.add(i); res.add(n//i)
res = sorted(list(res))
try: print(res[k-1])
except: print(0)

# 9506
import sys
inputs = sys.stdin.readline
while True:
    n = int(inputs())
    if n == -1: break
    else:
        res = set()
        for i in range(2, n//2):
            if n%i == 0:
                res.add(i); res.add(n//i)
        res = sorted(list(res))
        if sum(res)+1 == n:
            print(f'{n} = 1', end = '')
            for j in res:
                print(f' + {j}', end = '')
            print()
        else: print(f'{n} is NOT perfect.')

# 27323
import sys
inputs = sys.stdin.readline
a = int(inputs())
b = int(inputs())
print(int(a*b))

# 15894
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(n*4)