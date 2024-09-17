p = input("Qual é o país? ")
c = 0

while p != "China" and c < 6:
	c += 1
	if c < 2:
		print("Errrrrou!!\n")
		p = input("Qual é o país? ")
	else:
		if c == 2:
			print("Errrrrou!!\n")
			print("Dica: É um país asiático")
			p = input("Qual é o país? ")
		else:
			if c == 4:
				print("Errrrrou!!\n")
				print("Dica: Tem muitas pessoas")
				p = input("Qual é o país? ")
			else:
				if c == 5:
					print("Errrrrou!!\n")
					print("Dica: Terra do Mao Tsé-Tung")
					p = input("Qual é o país? ")
				else:
					if c == 6:
						print("\n去學地理")
					
if p == "China":
	print("\n恭喜")
	
