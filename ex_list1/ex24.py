g = input("Nome do(a) ginasta: ")

n1 = float(input("Nota 1: "))
maior = n1
menor = n1

n2 = float(input("Nota 2: "))
if n2 > maior:
	maior = n2
if n2 < menor:
	menor = n2

n3 = float(input("Nota 3: "))
if n3 > maior:
	maior = n3
if n3 < menor:
	menor = n3
	
n4 = float(input("Nota 4: "))
if n4 > maior:
	maior = n4
if n4 < menor:
	menor = n4
	
n5 = float(input("Nota 5: "))
if n5 > maior:
	maior = n5
if n5 < menor:
	menor = n5
	
n6 = float(input("Nota 6: "))
if n6 > maior:
	maior = n6
if n6 < menor:
	menor = n6
	
n7 = float(input("Nota 7: "))
if n7 > maior:
	maior = n7
if n7 < menor:
	menor = n7

if maior == int(maior):
    maior = int(maior)
if menor == int(menor):
    menor = int(menor)

m = (n1 + n2 + n3 + n4 + n5 + n6 + n7 - menor - maior) / 5
                            
print(f"\nA maior nota de {g} foi: {maior}\nA menor nota de {g} foi: {menor}\nE a média final de {g} foi: {m:.2f}")
