# 10815
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = set(map(int, inputs().split()))
m = int(inputs())
ll = list(map(int, inputs().split()))
for i in ll:
    if i in l: print(1, end = ' ')
    else: print(0, end = ' ')

# 14425
n, m = map(int, input().split())
ll = []; l = set(); count = 0
for i in range(n):
    l.add(input())
for j in range(m):
    ll.append(input())
for k in ll:
    if k in l: count += 1
print(count)

# 1620
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
l = {}; ll = {}
for i in range(n):
    txt =  inputs().strip()
    l[i+1] = txt; ll[txt] = i+1
for j in range(m):
    q = inputs().strip()
    try: print(l[int(q)])
    except: print(ll[q])

# 10816
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
dic = {}
for elem in l:
    dic[elem] = dic.get(elem, 0) + 1
m = int(inputs())
ll = list(map(int, input().split()))
for j in range(m):
    try: print(dic[ll[j]], end = ' ')
    except: print(0, end = ' ')

# 1764
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
l = set(); ll = set()
for i in range(n):
    l.add(inputs().strip())
for j in range(m):
    ll.add(inputs().strip())
res = list(sorted(l.intersection(ll)))
print(len(res))
print('\n'.join(res))

# 1269
import sys
inputs = sys.stdin.readline
n, m = map(int, inputs().split())
a = set(map(int, inputs().split()))
b = set(map(int, inputs().split()))
# ins = a.intersection(b)
# uni = a.union(b)
# res = uni.difference(ins)
res = a.symmetric_difference(b)
print(len(res))

# 11478
import sys
inputs = sys.stdin.readline
txt = inputs().strip()
n = len(txt); words = set()
for i in range(n):
    for j in range(1, n+1):
        word = txt[i:i+j]
        if word != '': words.add(word)
print(len(words))

# 13909
import sys
inputs = sys.stdin.readline
n = int(inputs())
print(int(n**0.5))