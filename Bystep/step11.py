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