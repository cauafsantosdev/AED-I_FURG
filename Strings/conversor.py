n = input("Digite seu nome: ")
c = 0

while c < len(n):
	if n[c] == " ":
		print(n[c], end="")
		c += 1
	else:
		if ord(n[c]) <= 90:
			print(chr(ord(n[c]) + 32), end="")
		else:
			print(chr(ord(n[c]) - 32), end="")
		c += 1

print()
