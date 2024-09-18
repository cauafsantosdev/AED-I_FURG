string = input("Digite algo: ")

for letra in string:
	if letra in " ,.!?0123456789":
		print(letra, end="")
	else:
		if ord(letra) <= 90:
			print(chr(ord(letra) + 32), end="")
		else:
			print(chr(ord(letra) - 32), end="")

print()