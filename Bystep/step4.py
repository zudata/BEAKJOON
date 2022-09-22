# 10818
n = int(input())
x = list(map(int, input().split()))
print(min(x), max(x))

# 2562
x = []
for i in range(9):
    x.append(int(input()))
print(max(x))
print(x.index(max(x))+1)

# 3052
x = []
for i in range(10):
    x.append(int(input())%42)
print(len(set(x)))

# 1546
n = int(input())
p = list(map(int, input().split()))
mx = max(p)
for i in range(n):
    p[i] = p[i]/mx*100
print(sum(p)/n)

# 8958
n = int(input())
for i in range(n):
    a = input()
    p = 0
    count = 0
    for j in range(len(a)):
        if a[j] == 'O': 
            count += 1
            p += count
        else: count = 0
    print(p)

# 4344
c = int(input())
for i in range(c):
    s = list(map(int, input().split()))
    n = s[0]
    s.pop(0)
    mean = sum(s)/n
    count = 0
    for j in range(n):
        if s[j] > mean: count += 1
    print(f'{count/n*100:.03f}%')