n = input("Digite seu nome: ")
c = 0

while c < len(n):
	if n[c] == " ":
		print()
		c += 1
	else:
		print(n[c], end="")
		c += 1

print()
