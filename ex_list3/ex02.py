frase = input("Digite uma frase: ").lower()
letra = 0

while letra < len(frase):
	if letra == 0:
		print(chr(ord(frase[letra]) - 32), end="")
		
	elif frase[letra] == " ":
		print(frase[letra], end="")
		letra += 1
		
		print(chr(ord(frase[letra]) - 32), end="")
		
	else:
		print(frase[letra], end="")
	letra += 1

print()