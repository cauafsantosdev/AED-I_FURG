n = input("Digite seu nome: ").lower()
c = 0

while c < len(n):
	if c == 0:
		print(chr(ord(n[c]) - 32), end="")
	elif n[c] == " ":
		print(n[c], end="")
		c += 1
		print(chr(ord(n[c]) - 32), end="")
	else:
		print(n[c], end="")
	c += 1

print()
