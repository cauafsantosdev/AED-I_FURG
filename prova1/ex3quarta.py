n = 0

while n < 1000 or n > 9999:
    n = int(input("Digite um número entre 1000 e 9999: "))
    
d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

print(f"{n} -> {d4}{d3}{d2}{d1}")
