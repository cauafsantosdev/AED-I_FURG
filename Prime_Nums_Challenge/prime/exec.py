from prime import fh
from prime import op


def menu():
    print("-" * 30)
    print(f"{'Pymos':^30}")
    print("-" * 30)
    print(f"{'[1] para verificar se um número é primo':>5}")
    print(f"{'[2] para ver série de números primos':>5}")
    print(f"{'[3] para ver números primos salvos':>5}")
    print(f"{'[4] para encontrar novo número primo':>5}")
    print(f"{'[5] para sair':>5}")
    print("-" * 30)

def option():
    choice = int(input("-> "))
    print()
    return choice

def main():
    while True:
        menu()
        choice = option()

        if choice == 1:
            n = 1

            while n <= 1:
                n = int(input("Insira um número inteiro positivo e maior que 1: "))
                print()
            
            if op.prime_check(n):
                print(f"{n} é um número primo\n")
            else:
                print(f"{n} não é um número primo\n")

        elif choice == 2:
            start = 1
            end = 0

            while start <= 1:
                start = int(input("Insira um número inteiro positivo e maior que 1: "))
                print()

            while end <= start:
                end = int(input("Insira um número inteiro positivo e maior que o de começo: "))
                print()

            print(", ".join(map(str, op.primes_between(start, end))))
            print()
        
        elif choice == 3:
            print(", ".join(map(str, fh.full_list())))
            print()

        elif choice == 4:
            print(op.next_prime())
            print()

        elif choice == 5:
            break

        else:
            print("OPÇÃO INVÁLIDA!\n")
