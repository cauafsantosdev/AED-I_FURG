x = input("Digite uma palavra: ")
y = input("Digite outra palavra: ")
anagrama = False

if len(x) == len(y):
    for i in range(0, len(y)):
        if x[i] in y:
            anagrama = True

if anagrama:
    print(f"{x} e {y} são anagramas")
else:
    print(f"{x} e {y} não são anagramas")