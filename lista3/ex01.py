frase = input("Digite uma frase: ")

for letra in frase:
    if letra in " ,.!?0123456789":
        print(letra, end="")
    else:
        if ord(letra) <= 90:
            print(letra, end="")
        else:
            print(chr(ord(letra) - 32), end="")

print()