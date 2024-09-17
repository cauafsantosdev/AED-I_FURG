n = int(input("Digite um número: "))
c = 1

print(f"Os divisores de {n} são: ", end="")

while c <= n:
	if n % c == 0:
		print(f"{c} ", end="")
	c += 1

print()
