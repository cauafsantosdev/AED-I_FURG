import random

sorteado = random.randint(1, 1000000)

n = int(input("Chute um número: "))

while n != sorteado:
    if n > sorteado:
        n = int(input("Chute mais baixo: "))
    else:
        if n < sorteado:
            n = int(input("Chute mais alto: "))

if n == sorteado:
    print("Parabéns, você acertou!")
