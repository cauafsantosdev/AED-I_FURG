matrix = []

print("- Matriz 5x10 -")

for i in range(1, 6):
    line = list(map(int, input(f"Informe os valores da {i}º linha, separados por vírgula: ").split(",")))
    matrix.append(line)

print()

for line in matrix:
    print(line)