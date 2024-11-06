numeros = input("Insira quantos números quiser, separados por vírgula: ").split(", ")
numeros = [i for i in numeros if int(i) % 2 == 0]

if len(numeros) > 0:
    print(f"\nOs números pares são: {", ".join(numeros)}")
else:
    print("\nNenhum número par foi digitado")