
#HORRIBLE BRUTE FORCE METHOD DO NOT USE
total = 0
for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

#BRILLIANT EFFICIENT METHOD USE THIS
sum3s = (333/2) * ((2*3) + (333-1)*3)
sum5s = (199/2) * ((2*5) + (199-1)*5) 
sum15s = (66/2) * ((2*15) + (66-1)*15)

print(sum3s + sum5s - sum15s)       