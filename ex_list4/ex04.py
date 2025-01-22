n = -1

while n < 0:
    n = int(input("Informe um número para achar seus divisores: "))

divisors = []
for i in range(n, 0, -1):
    if n % i == 0:
        divisors.append(i)

print(sorted(divisors))