lista1 = input("Insira uma lista com seus componentes separados por vírgulas: ").split(", ")
lista2 = input("\nInsira outra lista com seus componentes separados por vírgulas: ").split(", ")

comum = [i for i in lista1 if i in lista2]

print(f"\nOs elementos comuns à ambas as listas são: {", ".join(comum)}")