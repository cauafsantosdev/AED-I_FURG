def get_matrix(lines: int, collumns: list):
    matrix = []

    for i in range(1, lines+1):
        line = list(map(int, input(f"Linha {i}: ").split(",")))
        matrix.append(line[:collumns])

    return matrix

def matrix_multiply(matrix1: list, matrix2: list):
    if len(matrix2) != len(matrix1[0]):
        raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas de matriz B.")
    
    multiplied_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return multiplied_matrix


lines_a = int(input("Quantas linhas possui a matriz A? "))
collumns_a = int(input("Quantas colunas possui a matriz A? "))

print()
matrix1 = get_matrix(lines_a, collumns_a)

lines_b = int(input("\nQuantas linhas possui a matriz A? "))
collumns_b = int(input("Quantas colunas possui a matriz A? "))

print()
matrix2 = get_matrix(lines_b, collumns_b)
print()

for line in matrix_multiply(matrix1, matrix2):
    print(line)