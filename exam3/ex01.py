def get_matrix():
    matrix = []
    lines = int(input("Quantas linhas possui a matriz? "))

    for i in range(lines):
        line = list(map(int, input(f"Linha {i+1}: ").split(",")))
        matrix.append(line)
    
    return matrix

def validate_matrix(matrix: list):
    collumns = len(matrix[0])

    for i in range(1, len(matrix)):
        if len(matrix[i]) != collumns:
            return False
        
    return True

def diagonal_sum(matrix: list):
    for line in matrix:
        if len(line) != len(matrix):
            return None

    s = 0

    for i in range(len(matrix)):
        s += matrix[i][i]

    return s

def biggest_value(matrix: list):
    max_values = []

    for line in matrix:
        max_values.append(max(line))

    return max(max_values)

def most_frequent_value(matrix: list):
    all_values = []

    for line in matrix:
        for element in line:
            all_values.append(element)

    unique_values = set(all_values)
    most_frequent = [0, 0]

    for number in unique_values:
        frequence = all_values.count(number)
        if frequence > most_frequent[1]:
            most_frequent = [number, frequence]

    return most_frequent


matrix = get_matrix()

if validate_matrix(matrix):
    print("\nMatriz válida")
else:
    print("\nMatriz inválida")
    quit()

print(f"O maior valor da matriz é {biggest_value(matrix)}")

number, frequence = most_frequent_value(matrix)
print(f"O valor mais frequente na matriz é {number}, que aparece {frequence} vezes")

s = diagonal_sum(matrix)

if s != None:
    print(f"E a soma da diagonal principal da matriz é {s}")