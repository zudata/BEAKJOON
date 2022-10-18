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

# 1018
n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(input())
wc = "WB"*4 + "BW"*4
bc = "BW"*4 + "WB"*4
min = 2174000
for r in range(n-7):
    for c in range(m-7):
        c1 = 0; c2 = 0; sec = ""
        for row in b[r:r+8]:
            sec += row[c:c+8]
            if len(sec) == 16:
                for i in range(16):
                    if sec[i] != wc[i]: c1 += 1
                    elif sec[i] != bc[i]: c2 += 1
                sec = ""
        if c1 <= c2 and c1 < min: min = c1
        elif c2 < c1 and c2 < min: min = c2
print(min)

# 1436
nums = []
for num in range(666, 2700000):
    if '666' in str(num): nums.append(int(num))
nums.sort()
print(nums[int(input())-1])