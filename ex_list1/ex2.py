v = float(input("Quanto custará a viagem? R$"))
w = input("Terá wifi? ")
p = input("Terá piscina? ")
c = input("Terá churrasqueira? ")

if v < 0 or v > 30:
	print("\nA viagem NÃO ocorrerá")
else:
	if (w == "Não" or w == "Não terá") and (p == "Não" or p == "Não terá") and (c == "Não" or c == "Não terá"):
		print("\nA viagem NÃO ocorrerá")
	else:
		if (w == "Sim" or w == "Terá") and (p == "Sim" or p == "Terá"):
			print("\nA viagem ocorrerá")
		else:
			if (w == "Não" or w == "Não terá") or (p == "Não" or p == "Não terá") and (c == "Sim" or c == "Terá"):
				print("\nA viagem ocorrerá")
			else:
				if (w == "Sim" or w == "Terá") or (p == "Sim" or p == "Terá") and (c == "Sim" or c == "Terá"):
					print("\nA viagem ocorrerá")
	
