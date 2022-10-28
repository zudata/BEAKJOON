# 5086
import sys
inputs = sys.stdin.readline
while True:
    a, b = map(int, inputs().split())
    if a == b == 0: break
    elif b%a == 0: print('factor')
    elif a%b == 0: print('multiple')
    else: print('neither')

# 1037
import sys
inputs = sys.stdin.readline
n = int(inputs())
l = list(map(int, inputs().split()))
l.sort()
print(l[0]*l[n-1])