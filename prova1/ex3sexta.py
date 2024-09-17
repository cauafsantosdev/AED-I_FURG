n = int(input("Digite um número: "))

ultimo = s = n % 10
c = 10

if n > 10:
	while n // c != 0:
		digito = (n // c) % 10
		s += digito
		c *= 10
	print(f"{n} -> {s}")
else:
	print(f"{n} -> {s}")
		
