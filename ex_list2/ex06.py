def menu():
    print("-" * 30)
    print(f"{'BANCO DE DADOS DE TIMES':^30}")
    print("-" * 30)
    print("\n[1] para adicionar times\n[2] para remover times\n[3] para ver a lista de times\n[0] para sair")
    print("-" * 30)
    op = int(input(" -> "))
    print()

    return op


times = []

while True:
    op = menu()

    if op == 0:
        break
    elif op == 1:
        time = input("Nome do time: ")
        times.append(time)
        print(f"{time} foi adicionado à lista\n")
    elif op == 2:
        remover = input("Qual time deseja remover? ")

        if remover in times:
            times.remove(remover)
            print(f"{remover} foi removido da lista\n")
        else:
            print(f"{remover} não está na lista\n")
    elif op == 3:
        print("\n".join(f"{i}: {j}" for i, j in enumerate(times, start=1)))
        print()
    else:
        print("OPÇÃO INVÁLIDA! Tente novamente.\n")