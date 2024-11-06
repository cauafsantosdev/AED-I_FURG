n = int(input("Digite um número: "))

while n < 1:
    n = int(input("Digite um número positivo: "))

if n == 2 or n == 3 or n == 5 or n == 7:
    print(f"{n} é um número primo.")
elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
