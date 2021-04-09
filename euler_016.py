
def digitSum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    
    return total

print(digitSum(2**1000))