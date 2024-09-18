frase = input("Digite uma frase: ")
teste = frase.lower().replace(" ", "")
palindromo = ""

for i in range(len(teste)-1, -1, -1):
	palindromo += teste[i]

if palindromo == teste:
	print(f"{frase} é um palíndromo")
else:
    print(f"{frase} não é um palíndromo")