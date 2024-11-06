lista_num = []

while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        print()
        break
    else:
        lista_num.append(n)

soma_atual = 0
maior_soma = 0

for n in lista_num:
    if n % 2 != 0:
        soma_atual += n
    else:
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        soma_atual = 0
    
if soma_atual > maior_soma:
    maior_soma = soma_atual

print(f"A maior soma entre os números ímpares consecutivos foi de: {maior_soma}")
        