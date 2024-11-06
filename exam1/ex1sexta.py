desempenho = -1

while desempenho < 0:
    desempenho = float(input("Quantos Km/l seu carro faz? "))

trajeto = -1

while trajeto < 0:
    trajeto = int(input("Quantos Km foram percorridos no último mês? "))

gasto =  (trajeto / desempenho) * 5.85

print(f"\nO carro faz {desempenho:.2f}Km/l e percorreu {trajeto} no último mês, portanto foram gastos R${gasto:.2f} em gasolina.")


