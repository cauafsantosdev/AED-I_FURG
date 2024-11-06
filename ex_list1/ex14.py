u = int(input("Digite um número: "))
n = 0
c = 0

while n < u:
    n += 1
    while c < n:
        print(n, end="")
        c += 1
    
    c = 0
    print()
