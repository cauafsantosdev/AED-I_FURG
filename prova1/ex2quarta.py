d, m, a = input("Insira a data inicial (DD/MM/AAAA): ").split("/")

while (int(d) < 1 or int(d) > 31) or (int(m) < 1 or int(m) > 12) or (int(a) < 1):
    d, m, a = input("\nData inválida, tente novamente: ").split("/")
while int(m) == 2 and int(d) > 28:
    d, m, a = input("\nData inválida, tente novamente: ").split("/")
while (int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11) and int(d) >= 31:
    d, m, a = input("\nData inválida, tente novamente: ").split("/")

intervalo = int(input("Quantos dias à frente deseja calcular? "))
w = intervalo
x = int(d)
y = int(m)
z = int(a)

while intervalo > 0:
    while (y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12) and intervalo > 0:
        if x < 31:
            x += 1
            intervalo -= 1
        else:
            x = 1
            y += 1
            intervalo -= 1
    while (y == 4 or y == 6 or y == 9 or y == 11) and intervalo > 0:
        if x < 30:
            x += 1
            intervalo -= 1
        else:
            x = 1
            y += 1
            intervalo -= 1
    while y == 2 and intervalo > 0:
        if (z % 4 == 0 and z % 100 != 0) or z % 400 == 0:
            if x < 29:
                x += 1
                intervalo -= 1
            else:
                x = 1
                y += 1
                intervalo -= 1
        else:
            if x < 28:
                x += 1
                intervalo -= 1
            else:
                x = 1
                y += 1
                intervalo -= 1
    if y == 13:
        x = 1
        y = 1
        z += 1
        intervalo -= 1

if x < 10:
    x = f"0{x}"
if y < 10:
    y = f"0{y}"
print(f"{d}/{m}/{a} + {w} dias = {x}/{y}/{z}")
