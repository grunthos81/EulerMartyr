import time

start = time.time()

chains = {1:0, 2:1, 4:2}


def fillChains(thisChain, n):
    while len(thisChain) > 0:
        chains[thisChain[0]] = len(thisChain) + n
        del thisChain[0]

def getChain(n):
    thisChain = [n]
    currentNumber = n
    while True:
        if currentNumber % 2 == 0:
            currentNumber //= 2
        else:
            currentNumber = (currentNumber * 3) + 1
        
        if currentNumber in chains:
            break
        else:
            thisChain.append(currentNumber)
    
    fillChains(thisChain, chains[currentNumber])
    return chains[n]


n = 3
biggestChain = 0
biggestN = 0
while n < 1000000:
    if n not in chains:
        currentChain = getChain(n)
        if currentChain > biggestChain:
            biggestChain = currentChain
            biggestN = n
    n += 1

print("xxxx", time.time() - start)