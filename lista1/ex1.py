l = float(input("Informe a largura da figura: "))
c = float(input("Informe o comprimento da figura: "))

if l <= 0 or c <= 0:
	print("\nMedidas inválidas")
else:
	if l == c:
		print("\nÉ um quadrado")
	else:
			print("\nÉ um retângulo")
