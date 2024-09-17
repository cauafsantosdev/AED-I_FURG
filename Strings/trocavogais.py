x = input("Digite uma frase: ")
v = int(input("Digite 1 para A\nDigite 2 para E\nDigite 3 para I\nDigite 4 para O\nDigite 5 para U\n-> "))
c = 0

if v == 1:
	while c < len(x):
		n = x.lower()
		if n[c] == "e" or n[c] == "i" or n[c] == "o" or n[c] == "u":
			print("a", end='')
			c += 1
		else:
			print(n[c], end='')
			c += 1
elif v == 2:
	while c < len(x):
		n = x.lower()
		if n[c] == "a" or n[c] == "i" or n[c] == "o" or n[c] == "u":
			print("e", end='')
			c += 1
		else:
			print(n[c], end='')
			c += 1
elif v == 3:
	while c < len(x):
		n = x.lower()
		if n[c] == "a" or n[c] == "e" or n[c] == "o" or n[c] == "u":
			print("i", end='')
			c += 1
		else:
			print(n[c], end='')
			c += 1
elif v == 4:
	while c < len(x):
		n = x.lower()
		if n[c] == "a" or n[c] == "e" or n[c] == "i" or n[c] == "u":
			print("o", end='')
			c += 1
		else:
			print(n[c], end='')
			c += 1
elif v == 5:
	while c < len(x):
		n = x.lower()
		if n[c] == "a" or n[c] == "e" or n[c] == "i" or n[c] == "o":
			print("u", end='')
			c += 1
		else:
			print(n[c], end='')
			c += 1
else:
	print("Opção inválida")
	
print()
