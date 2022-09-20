# 1330
a, b = map(int, input().split())
if a >= -10000 and b <= 10000:
    if a > b: print('>')
    elif a < b: print('<')
    else: print('==')
else: a, b = map(int, input().split())

# 9498
a = int(input())
if a<=100 and a>=90 : print('A')
elif a >= 80 : print('B')
elif a >= 70 : print('C')
elif a >= 60 : print('D')
else: print('F')

# 2753
y = int(input())
if y%400 ==0 or (y%4 == 0 and y%100 != 0): print(1)
else: print(0)

# 14681
x = int(input())
y = int(input())

if x >= -1000 and x <= 1000 and y >= -1000 and y <= 1000:
    if x > 0 and y > 0: print(1)
    elif x < 0 and y > 0: print(2)
    elif x < 0 and y < 0: print(3)
    else: print(4)
else: x = int(input()); y = int(input())

# 2884
h, m = map(int, input().split())
if h >= 0 and h < 24 and m >= 0 and m < 60:
    m -= 45
    if m < 0:
        h -= 1
        m = 60 + m
    else: h
    if h < 0: h = 24 + h
    else: h
    print(h, m)
else: h, m = map(int, input().split())

# 2525
h, m = map(int, input().split())
c = int(input())
if h >= 0 and h < 24 and m >= 0 and m < 60 and c >= 0 and c <= 1000:
    hp = c//60; mp = c%60
    h += hp; m += mp
    if m > 59:
        h += 1
        m -= 60
    else: h
    if h > 23: h -= 24
    else: h
    print(h, m)
else: h, m = map(int, input().split()); c = int(input())

# 2480
i = list(map(int, input().split()))
if i[0] == i[1] == i[2]: money = 10000 + i[0] * 1000
elif i[0] != i[1] and i[0] != i[2] and i[1]!= i[2]: money = max(i) * 100
else:
    if i[0] != i[2]: money = 1000 + i[1] * 100
    else: money = 1000 + i[0] * 100
print(money)