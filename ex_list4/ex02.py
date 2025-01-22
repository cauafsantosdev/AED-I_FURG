size = -1

while size <= 0:
    size = int(input("Informe o tamanho da lista: "))

numbers = []
for i in range(1, size + 1):
    numbers.append(int(input(f"{i}º número: ")))

positives = [n for n in numbers if n > 0]
negatives = [n for n in numbers if n < 0]
zeros = [n for n in numbers if n == 0]

print(f"\nNúmeros positivos: {len(positives)}\nNúmeros negativos: {len(negatives)}\nZeros: {len(zeros)}")