nome = input("Digite seu nome: ").lower()
lista = nome.split()
nome = []
preposicao = ['de', 'da', 'do', 'das', 'dos', 'e']

for i in lista:
    if i in preposicao:
        nome.append(i)
    else:
        nome.append(i[0].upper())
    
        for j in range(1, len(i)):
            nome.append(i[j])
    
    nome.append(" ")

print(''.join(nome))
