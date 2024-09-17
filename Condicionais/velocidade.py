x = float(input("Insira a distância percorrida em metros: "))
y = float(input("Insira o tempo gasto em minutos: "))
z = float(y * 60)
v = x / z
v = v * 3.6

if v == int(v):
    v = int(v)
    print(f"A velocidade de deslocamento foi de {v}km/h")
else:
    print(f"A velocidade de deslocamento foi de {round(v, 2)}km/h")   
