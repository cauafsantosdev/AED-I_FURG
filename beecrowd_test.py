while True:
    n = int(input())

    if n == 0:
        break

    else:
        lista = []
        temporario = []

        for i in range(n):
            frase = input()
            temporario.append(" ".join(frase.split()))

        lista.append(temporario)
        
        espacos = []
        caracteres = len(max(temporario, key=len))
        espacos.append(caracteres)
            
        for i in range(n):
            frase = lista[i]
            print(f"{frase.rjust(caracteres)}")
        
        print()