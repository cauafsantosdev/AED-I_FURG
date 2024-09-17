idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade >= 18:
	print("Pode beber cerveja!")
	carteira = input("Possui carteira de motorista? ")
	if carteira == 'sim' or carteira == 's' or carteira == 'possuo':
		print("Pode dirigir!")
	else:
		print("Vá de ônibus!")
else: 
	print("Não pode beber cerveja, nem dirigir!")
