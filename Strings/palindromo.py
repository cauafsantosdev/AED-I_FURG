x = input("Digite uma frase: ")
frase = x.lower().replace(" ", "")
palindromo = ""
c = len(frase) - 1

while c >= 0:
	palindromo += x[c]
	c -= 1

if palindromo == x:
	print(f"{x} é um palíndromo")
else:
    print(f"{x} não é um palíndromo")