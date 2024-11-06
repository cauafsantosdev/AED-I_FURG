n = int(input("Digite um número: "))
c = 0

print(f"\nOs seis números ímpares após {n} são:", end=" ")

while c <= 6:
    n += 1
    if n % 2 != 0:
        c += 1
        if c < 5:
            print(n, end=', ')
        else:
            if c == 5:
                print(n, end=' ')
            else:
                if c == 6:
                    print(f"e {n}")
