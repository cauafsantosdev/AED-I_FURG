n = 0

while n == 0:
    n = int(input("Informe um número inteiro positivo: "))
    
while n > 1:
    n = n / 2
    if n < 1:
        print(f"Chegou a zero!")
    else:
        print(f"Resultado da divisão: {n:.2f}")
