a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

if a <= b + c and b <= + c and c <= a + b:
	if a == b == c:
		print("\nTriângulo equilátero")
	else:
		if a == b or b == c or c == a:
			print("\nTriângulo isósceles")
		else:
				print("\nTriangulo escaleno")
else:
	print("\nNão é um triângulo")
