# 2798
n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cards = card[i] + card[j] + card[k]
            if cards <= m and cards >= res: res = cards
print(res)

# 2231
n = int(input())
res = 0
for i in range(1, n+1):
    l = list(map(int, str(i)))
    s = i + sum(l)
    if s == n:
        res = i
        break
print(res)

# 7568
l = [list(map(int, input().split())) for i in range (int(input()))]
rank = [0]*len(l)
for i in range(len(l)):
    r = 1
    x,y = l[i]
    for j in l:
        if j[0] > x and j[1] > y:
            r += 1
    rank[i] = str(r)
print(" ".join(rank))