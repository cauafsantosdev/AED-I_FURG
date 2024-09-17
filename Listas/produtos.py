lista = []
s = 0

print("Insira quantos produtos quiser, ao terminar digite fim\n")

while True:
	produto = input("Insira um produto: ").title()
	if produto == "Fim":
		break
	else:
		preco = float(input(f"Insira o preço de {produto}: R$"))
		s += preco
		print(f"{produto} adicionado à lista\n")
		lista.append(produto)
		lista.append(preco)

print(f"\n{'LISTA DE PRODUTOS:':^35}")

for i in range(0, len(lista), 2):
	print(f"{lista[i]:.<30}R${lista[i + 1]:.2f}")

print(f"\n{'Total':.<30}R${s:.2f}")
