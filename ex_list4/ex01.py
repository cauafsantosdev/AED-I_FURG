size = -1

while size <= 0:
    size = int(input("Informe o tamanho da lista: "))

numbers = []
for i in range(1, size + 1):
    numbers.append(int(input(f"{i}º número: ")))

positives = sorted(list(set([n for n in numbers if n >= 0])))
negatives = sorted(list(set([n for n in numbers if n < 0])))

print(f"\nNúmeros positivos: {positives}\nNúmeros negativos: {negatives}")