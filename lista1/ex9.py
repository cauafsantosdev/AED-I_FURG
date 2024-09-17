while True:
    r = float(input("Minha renda é de R$"))

    if r <= 0:
        print("Valor inválido, tente novamente.\n")
    else:
        break

t = int(input("\nDigite 1 para o valor sem correção;\nDigite 2 para o valor com correção das perdas no governo Bolsonaro;\nDigite 3 para o valor com correção integral;\nOu digite 4 para ver todos os valores.\n-> "))

if t == 1 or t == 4:
    if r <= 1903.98:
        print("\nSem correção: isento")
    else:
        if r >= 1903.99 and r <= 2826.65:
            print("\nSem correção: Pagar R$142,80 (7,50%)")
        else:
            if r >= 2826.66 and r <= 3751.05:
                print("\nSem correção: Pagar R$354,80 (15%)")
            else:
                if r >= 3751.06 and r<= 4664.68:
                    print("\nSem correção: Pagar R$636,13 (22,50%)")
                else:
                    if r > 4664.68:
                        print("\nSem correção: Pagar R$869.36 (27.50%)")

if t == 2:
    print()

if t == 2 or t == 4:
    if r <= 2500.44:
        print("Com correção das perdas no governo Bolsonaro: isento")
    else:
        if r >= 2500.45 and r <= 3712.16:
            print("Com correção das perdas no governo Bolsonaro: Pagar R$187.54 (7,50%)")
        else:
            if r >= 3712.17 and r <= 4926.14:
                print("Com correção das perdas no governo Bolsonaro: Pagar R$465.95 (15%)")
            else:
                if r >= 4926.15 and r <= 6125.99:
                    print("Com correção das perdas no governo Bolsonaro: Pagar R$835.41 (22.50%)")
                else:
                    if r > 6125.99:
                        print("Com correção das perdas no governo Bolsonaro: Pagar R$1141.71 (27,50%)")

if t == 3:
    print()

if t == 3 or t == 4:
    if r <= 4710.49:
        print("Com correção integral: isento")
    else:
        if r >= 4710.50 and r <= 6993.20:
            print("Com correção integral: Pagar R$353.29 (7.50%)")
        else:
            if r >= 6993.21 and r <= 9280.19:
                print("Com correção integral: Pagar R$877.78 (15%)")
            else:
                if r >= 9280.20 and r <= 11540.53:
                    print("Com correção integral: Pagar R$1573.80 (22.50%)")
                else:
                    if r > 11540.53:
                        print("Com correção integral: Pagar R$2150.82 (27.50%)")
