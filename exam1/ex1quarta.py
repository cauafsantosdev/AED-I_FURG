l = 0
c = 0

while (l <= 0 or c <= 0) or l == c:
    l = float(input("Informe a largura do retângulo: "))
    c = float(input("Informe o comprimento do retângulo: "))
    if l == c:
        print("As duas medidas não podem ser iguais\n")
    elif l <= 0 or c <= 0:
        print("As medidas devem ser valores positivos\n")

print(f"\nA área do retângulo de {l:.2f}x{c:.2f} é {l * c:.2f}")
