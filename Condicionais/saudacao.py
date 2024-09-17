nome = str(input("Digite seu nome: "))
hora = int(input("Digite a hora do dia: "))

if hora > 24 or hora <= -1:
	print("Horário inválido")
elif hora >= 5 and hora <= 12:
	print("Bom dia, " + nome)
elif hora >= 13 and hora <= 18:
	print("Boa tarde, " + nome)
else:
	print("Boa noite, " + nome)
