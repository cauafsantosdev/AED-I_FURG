list1 = list(map(int, input("Informe 5 números inteiros em ordem crescente, separados por vírgula: ").split(",")))
list2 = list(map(int, input("Informe 5 números inteiros em ordem crescente, separados por vírgula: ").split(",")))

list3 = sorted(list1 + list2)

print(f"{list3}\n{sum(list3)}")