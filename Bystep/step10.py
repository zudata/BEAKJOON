# 10872
def fact(n):
    result = 1
    if n > 0 :
        result = n*fact(n-1)
    return result
n = int(input())
print(fact(n))

# 10870
def fibo(n):
    result = 1
    if n == 1: result = 1
    elif n > 1: result = fibo(n-1) + fibo(n-2)
    else: result = 0
    return result
n = int(input())
print(fibo(n))