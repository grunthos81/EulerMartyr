total = 2

t1 = 1
t2 = 2
while t2 < 4000000:
    t3 = t2 + t1
    if t3 % 2 == 0:
        total += t3
    t1 = t2
    t2 = t3

print(total)