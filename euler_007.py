
def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    
    d = 2
    while d*d < n:
        if primes[d]:
            for i in range(2*d, n, d):
                primes[i] = False
            
        d += 1
    
    return primes

limit = 150000
primeNumbers = sieve(limit)
count = 0
for i in range(2, limit):
    if primeNumbers[i]:
        count += 1
        if count == 10001:
            print(i)
            break
        
        
