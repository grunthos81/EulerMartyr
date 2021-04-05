
def numberOfDivisors(n):
    d = 2
    divisors = {0:0}
    while n != d:
        if n % d == 0:
            if d in divisors:
                divisors[d] += 1
            else:
                divisors[d] = 1
            n //= d
        else:
            if d == 2:
                d += 1
            else:
                d += 2
    
    divisors[d] = 1
    
    product = 1
    for k, v in divisors.items():
        product *= (v + 1)
    
    return product

n = 3
a = 3
while numberOfDivisors(n) < 500:
    n += a
    a += 1

print(n)