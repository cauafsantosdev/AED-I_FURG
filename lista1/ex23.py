x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

while x > y or x == y or x < 0 or y < 0:
	print("\nO primeiro número deve ser menor que o segundo e os valores não podem ser negativos.")
	x = int(input("Digite um número positivo: "))
	y = int(input("Digite um número positivo maior que o anterior: "))

print(f"\nOs números primos entre {x} e {y} são:")

while x < y:
    if x == 2 or x == 3 or x == 5 or x == 7:
        print(x, end=" ")
        x += 1
    else:
        x += 1
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
            print(x, end=" ")
        if x == y:
            print()
