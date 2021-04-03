import time

start = time.time()
biggest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i*j
        if str(n) == str(n)[::-1] and n > biggest:
            biggest = n

print(biggest, time.time() - start)

mid = time.time()

found = False
n = 999
while not found:
    currentNumber = int(str(n) + str(n)[::-1])
    j = 999
    while j > 99:
        if currentNumber % j == 0 and currentNumber // j in range(100, 1000):
            print(currentNumber, time.time() - mid)
            found = True
            break
        else:
            j -= 1
    
    n -= 1


        
        
        
        
        
        
        
        
        