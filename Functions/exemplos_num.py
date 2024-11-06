def dobro(n: float):
    return n * 2 if (n * 2) % 1 != 0 else int(n * 2)

def par_check(n: int):
    return n % 2 == 0

def tabuada(n: int):
    saida = ''
    for i in range(11):
        saida += f"{n} x {i} = {n * i}\n"
    return saida

def tabuada_entre(start: int, end: int):
    saida = ''
    for i in range(start, end+1):
        for j in range(11):
            saida += f"{i} x {j} = {i * j}\n"
        if i != end:
            saida += "\n"
    return saida

def primo_check(n: int):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


print(dobro(float(input("Digite um número para ver seu dobro: "))))
print()

if par_check(int(input("Digite um número para ver se o mesmo é par: "))):
    print("PAR!\n")
else:
    print("ÍMPAR!\n")

print(tabuada(int(input("Digite um número para ver sua tabuada: "))))

n1 = int(input("Digite o número de começo da sequência: "))
n2 = int(input("Digite o número de final da sequência: "))
print()
print(tabuada_entre(n1, n2))

if primo_check(int(input("Digite um número para ver se o mesmo é primo: "))):
    print("PRIMO!")
else:
    print("NÃO É PRIMO!")