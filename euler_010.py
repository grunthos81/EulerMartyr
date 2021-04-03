
def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    d = 2
    while d * d < n:
        if primes[d]:
            for i in range(2*d, n, d):
                primes[i] = False
            
        if d == 2:
            d = 3
        else:
            d += 2
    
    return primes

limit = 2000000
total = 0
listOfPrimes = sieve(limit)
for i in range(2, limit):
    if listOfPrimes[i]:
        total += i

print(total)






