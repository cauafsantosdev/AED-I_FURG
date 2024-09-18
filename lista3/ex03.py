frase = input("Digite uma frase: ")
c = len(frase)

while c > 0:
	print(frase[c - 1], end='')
	c -= 1

print()