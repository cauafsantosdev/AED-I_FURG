def get_matrix(lines: int, collumns: list):
    matrix = []

    for i in range(1, lines+1):
        line = list(map(int, input(f"Linha {i}: ").split(",")))
        matrix.append(line[:collumns])

    return matrix

def matrix_sum(matrix1: list, matrix2: list):
    summed_matrix = []

    for i in range(len(matrix1)):
        line = []
        for j in range(len(matrix1[i])):
            line.append(matrix1[i][j] + matrix2[i][j])
        summed_matrix.append(line)

    return summed_matrix


lines = int(input("Quantas linhas possuem as matrizes? "))
collumns = int(input("Quantas colunas possuem as matrizes? "))

print()
matrix1 = get_matrix(lines, collumns)
print()
matrix2 = get_matrix(lines, collumns)
print()

for line in matrix_sum(matrix1, matrix2):
    print(line)