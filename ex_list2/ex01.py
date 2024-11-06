palavras = input("Insira quantas palavras quiser, separadas por vírgula: ").split(", ")

palavras = [i for i in palavras if len(i) > 5]

if len(palavras) > 0:
    print(f"\nAs palavras com mais de 5 caracteres são: {", ".join(palavras)}")
else:
    print("\nNenhuma palavra digitada possui mais de 5 caracteres")