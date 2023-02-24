# 15596
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return(ans)

# 4673
s = set(range(1, 10001))
for n in range(1, 10001):
    for i in str(n):
        n += int(i)
    s.discard(n)
for j in s:
    print(j)

# 1065
n = int(input())
if n < 100: count = n
else:
    count = 99
    for i in range(100, n+1):
        string = []
        for j in str(i):
            string.append(j)
        if int(string[1])*2 == int(string[0]) + int(string[2]): count += 1
print(count)

# 2444
import sys
inputs = sys.stdin.readline
n = int(inputs())
for i in range(n):
    print(f'{" "*(n-i-1)}{"*"*(2*(i+1)-1)}')
for i in range(n-2, -1, -1):
    print(f'{" "*(n-i-1)}{"*"*(2*(i+1)-1)}')