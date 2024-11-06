frase = input("Digite uma frase: ")

frase_corrigida = ""

for idx, letra in enumerate(frase):
    if letra == " " and frase[idx+1] == " ":
        frase_corrigida += ""
    else:
        frase_corrigida += letra

print(frase_corrigida)