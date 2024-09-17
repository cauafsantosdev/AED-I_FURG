senha = input("Digite a senha: ")
c = 1

while senha != "internacional" and c < 5:
	c = c + 1
	print("Senha incorreta\n")
	senha = input("Tente novamente: ")
	if senha != "internacional" and c == 5:
		print("Acesso negado.")

if senha == "internacional":
	print("Acesso autorizado!")
