texto = input("Insira texto: ").replace(",", "").replace(".", "").split()

palavras = []
palavras = [i for i in texto if i not in palavras]

print()
print("\n".join(f"{i} aparece {texto.count(i)}" for i in palavras))