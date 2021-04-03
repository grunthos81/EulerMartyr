n = 600851475143
d = 3

while n != d:
    if n % d == 0:
        n //= d
    else:
        d += 2

print(n)