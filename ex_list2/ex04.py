lista_num = []

while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        break
    elif n not in lista_num:
        lista_num.append(n)

print(f"\n{len(lista_num)} números diferentes foram digitados")