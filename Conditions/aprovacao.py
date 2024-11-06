n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))
f = float(input("Informe a porcentagem de frequência: "))

if ((n1 + n2 + n3 + n4) / 4 >= 7) and f >= 75:
	print("Aprovado")
elif ((n1 + n2 + n3 + n4) / 4 >= 3 ) and f >= 75:
	print("Exame")
else:
	print("Reprovado")
