compras = []

print("Faça sua lista de produtos, ao terminar digite fim\n")

while True:
	produto = input("Insira um produto: ").title()
	if produto == "Fim":
		break
	else:
		print(f"{produto} adicionado à lista de compras\n")
		compras.append(produto)

print()

for i, p in enumerate(compras):
	print(f"{i + 1} - {p}")
