n = int(input("Digite um número: "))
fat = 1
c = 1

while c <= n:
    fat *= c
    c += 1
    
print(fat)
