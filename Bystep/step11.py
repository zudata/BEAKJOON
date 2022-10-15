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