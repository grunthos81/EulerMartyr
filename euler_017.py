units = [0,3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

total = 11

for i in range(1, 1000):
    if i > 99 and i % 100 == 0:
        total += units[i // 100] + 7
    elif i > 99:
        total += units[i // 100] + 10
        
    if i % 100 >= 20:
        total += tens[(i%100)//10] + units[i%10]
    else:
        total += units[i%100]


print(total)
