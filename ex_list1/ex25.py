n = 9

while n < 100:
    n += 1
    d1 = n // 10
    d2 = n % 10
    if (d1 == 1 or d1 == 2 or d2 == 1 or d2 == 2) and n % 3 == 0:
        print(n, end=" ")
                
print()
