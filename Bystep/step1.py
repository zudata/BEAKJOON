# 2557
print('Hello World!')

#10718
m = '강한친구 대한육군'
print(m + '\n' + m)

# 1000
a, b = map(int, input().split())
print(a + b)

# 1001
a, b = map(int, input().split())
print(a - b)

# 10998
a, b = map(int, input().split())
print(a*b)

# 1008
a, b = map(int, input().split())
print(a/b)

# 10869
a, b = map(int, input().split())
qs = [a+b, a-b, a*b, a/b, a%b]
for q in qs:
    print(int(q), end = '\n')

# 10926
print(input() + '??!')

# 18108
y = int(input())
if y >= 1000 and y <= 3000:  print(y - 543)
else: y = int(input())

# 3003
k, q, l, b, n, p = map(int, input().split())
print(1-k, 1-q, 2-l, 2-b, 2-n, 8-p)

# 10430
A, B, C = map(int, input().split())
answer = [(A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C]
for a in answer:
    print(a, end = '\n')

# 2588
a = int(input())
b1, b2, b3 = map(int, input())
answer = [a*b3, a*b2, a*b1, a*b3 + a*b2*10 + a*b1*100]
for a in answer:
    print(a, end = '\n')

# 10171
cat = ['\\    /\\', " )  ( ')", '(  /  )', ' \(__)|']
for a in cat:
    print(a, end = '\n')

# 10172
dog = ["|\\_/|", "|q p|   /}", '( 0 )"""\\', '|"^"`    |', "||_/=\\\\__|"]
for a in dog:
    print(a, end = '\n')

# 25083
sprout = ["         ,r\'\"7", "r`-_   ,\'  ,/", " \\. \". L_r\'", "   `~\\/", "      |", "      |"]
for a in sprout:
    print(a, end = '\n')