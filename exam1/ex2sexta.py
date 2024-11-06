d, m, a = input("Informe uma data de 2024 ou 2025 (DD/MM/AAAA): ").split("/")


while (int(d) < 1 or int(d) > 31) or (int(m) < 1 or int(m) > 12) or (int(a) < 2024 or int(a) > 2025):
    d, m, a = input("\nData inválida, tente novamente: ").split("/")
while int(m) == 2 and int(d) > 28 and int(a) == 2025:
    d, m, a = input("\nData inválida, tente novamente: ").split("/")
while int(m) == 2 and int(d) > 29 and int(a) == 2024:
    d, m, a = input("\nData inválida, tente novamente: ").split("/")
while (int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11) and int(d) >= 31:
    d, m, a = input("\nData inválida, tente novamente: ").split("/")

x = d
y = m
z = a
d = int(d)
m = int(m)
a = int(a)

if a == 2024:
	if m == 1 or m == 4 or m == 7:
		while d > 7:
			d -= 7
		if d == 7:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 2 or m == 8:
		while d > 7:
			d -= 7
		if d == 4:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 3 or m == 11:
		while d > 7:
			d -= 7
		if d == 3:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 5:
		while d > 7:
			d -= 7
		if d == 5:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado") 
	elif m == 9:
		while d > 7:
			d -= 7
		if d == 1:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado") 
	elif m == 10:
		while d > 7:
			d -= 7
		if d == 6:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado") 
	elif m == 9 or m == 12:
		while d > 7:
			d -= 7
		if d == 1:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
else:
	if m == 1 or m == 10:
		while d > 7:
			d -= 7
		if d == 5:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 2 or m == 3 or m == 11:
		while d > 7:
			d -= 7
		if d == 2:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é umaa terça-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 4 or m == 7:
		while d > 7:
			d -= 7
		if d == 6:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 5:
		while d > 7:
			d -= 7
		if d == 4:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 6:
		while d > 7:
			d -= 7
		if d == 1:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 8:
		while d > 7:
			d -= 7
		if d == 3:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 6:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 7:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
	elif m == 9 or m == 12:
		while d > 7:
			d -= 7
		if d == 7:
			print(f"{x}/{y}/{z} é um domingo")
		elif d == 1:
			print(f"{x}/{y}/{z} é uma segunda-feira")
		elif d == 2:
			print(f"{x}/{y}/{z} é uma terça-feira")
		elif d == 3:
			print(f"{x}/{y}/{z} é uma quarta-feira")
		elif d == 4:
			print(f"{x}/{y}/{z} é uma quinta-feira")
		elif d == 5:
			print(f"{x}/{y}/{z} é uma sexta-feira")
		else:
			print(f"{x}/{y}/{z} é um sábado")
		 
