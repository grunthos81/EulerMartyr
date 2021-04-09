import math

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def digitSum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(digitSum(math.factorial(100)))
print(digitSum(factorial(100)))