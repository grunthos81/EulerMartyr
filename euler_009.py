for m in range(1, 22):
    for n in range(1, 22):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a + b + c == 1000:
            print(a*b*c)
            m = 22
            break