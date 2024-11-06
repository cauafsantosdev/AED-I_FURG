lista_num = []

while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        print()
        break
    else:
        lista_num.append(n)

for i in range(min(lista_num), max(lista_num)+1):
    if i in lista_num:
        c = lista_num.count(i)
        if c == 1:
            print(f"O número {i} aparece {c} vez")
        else:
            print(f"O número {i} aparece {c} vezes")