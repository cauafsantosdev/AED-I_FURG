from random import shuffle

x = input("Digite um nome: ")
anagrama = [i for i in x]

shuffle(anagrama)
anagrama = "".join(anagrama)

print(anagrama)