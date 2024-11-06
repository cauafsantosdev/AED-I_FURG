print("Insira os números para a média, ao finalizar insira 0\n")

n = 1
s = 0
c = 0

while n != 0:
    n = float(input("Digite um número: "))
    s += n
    if n != 0:
    	c += 1

print(f"A média é: {s / c:.2f}")
