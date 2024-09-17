ano = int(input("Digite seu ano de nascimento: "))
i = 2024 - ano

if i <= 0 or i >= 120:
	print("Idade inválida")

else:
	if i > 0 and i < 16:
		print("Não pode votar!")
	else:
		if i >= 16 and i < 18 or i >= 70:
			print("Voto facultativo")
		else:
			if i >= 18 and i <= 69:
				print("Voto obrigatório")
