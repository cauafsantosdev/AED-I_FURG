x = input("Digite seu nome: ")
c = 0
v = 0

print()

while c < len(x):
	n = x.lower()
	if n[c] == "a" or n[c] == "e" or n[c] == "i" or n[c] == "o" or n[c] == "u":
		print(n[c], end=' ')
		c += 1
		v += 1
	else:
		c += 1

print(f"\n{x} possui {v} vogais\nComposto por {100 * (v / len(x)):.2f}% de vogais")
