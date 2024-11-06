import random


letras = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
num = "0123456789"
senha = []

print("-" * 30)
print(f"{'GERADOR DE SENHAS':^30}")
print("-" * 30)

while True:
    x = input("Deseja que a senha contenha letras? [S/N] ")
    if x in "SsNn":
        break

while True:
    y = input("Deseja que a senha contenha números? [S/N] ")
    if y in "SsNn":
        break

while True:
    z = int(input("Qual o tamanho da senha? "))
    if z > 0:
        break

if x in "Ss" and y in "Nn":
    senha += [random.choice(letras) for _ in range(z)]
    random.shuffle(senha)
elif x in "Nn" and y in "Ss":
    senha += [random.choice(num) for _ in range(z)]
    random.shuffle(senha)
else:
    senha = [random.choice(letras), random.choice(num)]
    senha += [random.choice(letras + num) for _ in range(z - 2)]
    random.shuffle(senha)

print(f"Senha gerada {''.join(senha)}")