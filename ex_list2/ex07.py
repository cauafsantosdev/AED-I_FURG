def menu():
    print("-" * 30)
    print(f"{'RESERVA DE INGRESSOS':^30}")
    print("-" * 30)
    print("\n[1] para reservar ingressos\n[2] para ver disponibilidade de lugares\n[3] para ver a lista de lugares reservados\n[0] para sair")
    print("-" * 30)
    op = int(input(" -> "))
    print()

    return op

sala = [["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["B", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["C", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["D", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["E", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["G", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["H", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["I", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            ["J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]

while True:
    op = menu()

    if op == 0:
        break
    elif op == 1:
        fileira = input("Escolha uma fileira: ")
        poltrona = input("Escolha uma poltrona: ")
        
        for i in sala:
            if fileira in i:
                i[int(poltrona)] = "X"
        print()
    
    elif op == 2:
        for fileira in sala:
            print(" ".join(fileira))
        print()

    elif op == 3:
        print(f"{'LUGARES RESERVADOS':^30}")
        print("-" * 30)

        for fileira in sala:
            for idx, poltrona in enumerate(fileira):
                if "X" in poltrona:
                    print(f"{fileira[0]}-{idx}")
        print()