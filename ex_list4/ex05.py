x = -1
y = -1

while x < 0:
    x = int(input("Informe a base: "))

while y < 0:
    y = int(input("Informe o expoente: "))

power = 1
for i in range(y):
    power *= x

print(power)