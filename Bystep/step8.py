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