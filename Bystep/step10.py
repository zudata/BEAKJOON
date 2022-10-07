# 10872
def fact(n):
    result = 1
    if n > 0 :
        result = n*fact(n-1)
    return result
n = int(input())
print(fact(n))