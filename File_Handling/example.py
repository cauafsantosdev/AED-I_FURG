with open('File_Handling/alunos.csv', 'r') as file:
    data = []

    for line in file.readlines():
        student = line.strip().split(";")
        if student[0] == "Matrícula":
            continue
        data.append(student)

for student in data:
    print(f"{student[0]:<6} | {student[1]:^10} | {student[2]}")

print()

for student in data:
    print(student[1])

print()

youngest = sorted(data, key=lambda x:x[2], reverse=True)[0]
print(f"{youngest[0]} | {youngest[1]} | {youngest[2]}")
