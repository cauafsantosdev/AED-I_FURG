d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))

if (d < 1 or d > 31) or (m < 1 or m > 12) or (a < 1):
    print("\nData inválida")
else:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        b = "ano bissexto"
    else:
        b = "ano não é bissexto"

    if b == "ano bissexto" and m == 2 and d <= 29:
        print(f"\n{d}/0{m}/{a} - Data válida, {b}")
    else:
        if m == 2 and d > 28:
            print("\nData inválida")
        else:
            if (m == 4 or m == 6 or m == 9 or m == 11) and d >= 31:
                print("\nData inválida")
            else:
                if d < 10:
                    d = "0" + str(d)
                if m <= 9:
                    print(f"\n{d}/0{m}/{a} - Data válida, {b}")
                else:
                    print(f"\n{d}/{m}/{a} - Data válida, {b}")
