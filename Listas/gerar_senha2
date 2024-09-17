import random


def menu():
    print("-" * 30)
    print(f"{'GERADOR DE SENHAS':^30}")
    print("-" * 30)


def strength():
    alpha = False
    num = False
    while True:
        x = input("Deseja que a senha contenha letras? [S/N] ")
        if x in "Ss":
            alpha = True
            break
        elif x in "Nn":
            break

    while True:
        y = input("Deseja que a senha contenha números? [S/N] ")
        if y in "Ss":
            num = True
            break
        elif y in "Nn":
            break

    while True:
        z = int(input("Qual o tamanho da senha? "))
        if z > 0:
            break
    
    return alpha, num, z


def senha(x=False, y=False, z=0):
    letras = "AaBbCcDdEeFfGgHhIiJjKkLlMMNnOoPpQqRrSsTtUuVvWwXxYyZz"
    num = "0123456789"
    senha = []

    if x and not y:
        senha += [random.choice(letras) for _ in range(z)]
        random.shuffle(senha)

    elif y and not x:
        senha += [random.choice(num) for _ in range(z)]
        random.shuffle(senha)
    
    else:
        senha = [random.choice(letras), random.choice(num)]
        senha += [random.choice(letras + num) for _ in range(z - 2)]
        random.shuffle(senha)

    return "".join(senha)


menu()
x, y, z = strength()
print(f"Senha gerada: {senha(x, y, z)}")