n = input("Digite o nome do funcionário: ")
s = float(input(f"Digite o salário de {n}: "))
ms = menor = maior = s
rico = pobre = n
c = 1
g1 = "ganha"
g2 = "ganha"

while n != "fim":
	n = input("Digite o nome do funcionário: ")
	if n == "fim":
		print(f"\nO maior salário é o de {rico}, que {g1} R${maior:.2f}.\nO menor salário é o de {pobre}, que {g2} R${menor:.2f}.\nE a média salárial da empresa é de R${ms / c:.2f}.")
	else:
		s = float(input(f"Digite o salário de {n}: "))
		ms = s + ms
		c = c + 1
		if menor > s:
		    menor = s
		    pobre = n
		else:
		    if menor == s:
		        pobre = pobre + " e " + n
		        g1 = "ganham"
		if maior < s:
		    maior = s
		    rico = n
		else:
		    if maior == s:
		        rico = rico + " e " + n
		        g2 = "ganham"
