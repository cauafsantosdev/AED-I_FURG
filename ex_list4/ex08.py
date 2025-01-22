def print_matrix(matrix: list):
    for line in matrix:
        print(line)

def max_matrix_value(matrix: list):
    max_values = []
    for line in matrix:
        max_values.append(max(line))
    
    return max(max_values)


list1 = list(map(int, input("Informe 5 números inteiros, separados por vírgula: ").split(",")))
list2 = list(map(int, input("Informe 5 números inteiros, separados por vírgula: ").split(",")))
list3 = list(map(int, input("Informe 5 números inteiros, separados por vírgula: ").split(",")))

matrix_lines = [list1, list2, list3]

matrix_collumns = []
for i in range(5):
    line = [list1[i], list2[i], list3[i]]
    matrix_collumns.append(line)

print()
print_matrix(matrix_lines)
print()
print_matrix(matrix_collumns)
print()
print(f"Maior valor contido na matriz: {max_matrix_value(matrix_lines)}")