texto = input("Insira texto: ")

caracteres = len(texto)
palavras = texto.split()
frases = 0

for i in texto:
    if i in ".!?":
        frases += 1

print(f"\nTotal de caracteres: {caracteres}\nTotal de palavras: {len(palavras)}\nTotal de frases: {frases}")