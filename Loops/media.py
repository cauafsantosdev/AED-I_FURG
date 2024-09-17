n = int(input("Digite um número: "))
maior = s = n
c = 1

while n != 0:
	n = int(input("Digite um número: "))
	if n > maior:
		s += n
		c += 1
		maior = n

print(f"A média é {s / c:.2f}")

