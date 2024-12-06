def find_uf(search: str): # Procura a UF de um estado através do nome
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        for state in data:
            if state[1] == search:
                return state[2]
        return None

def find_state(search: str): # Procura o nome de um estado através da UF
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        for state in data:
            if state[2] == search:
                return state[1]

def get_state_codes(): # Retorna os códigos dos estados segundo o IBGE
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

    return sorted([[state[0], state[1]] for state in data])

def find_state_by_code(code: str): # Procura o nome do estado através do código
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        for state in data:
            if state[0] == code:
                return state[1]

def shortest_state(): # Retorna o estado com nome mais curto
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        return min(data, key=lambda state: len(state[1]))[1]

def longest_state(): # Retorna o estado com nome mais longo
    with open("File_Handling/estados.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        return max(data, key=lambda state: len(state[1]))[1]

def cities_from_state(code: str): # Retorna o número de cidades de um determinado estado
    with open("File_Handling/municipios.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        return sum(1 for city in data if city[0] == code)

def cities_with_name(name: str): # Retorna AS cidades que possuem uma palavra específica no nome
    with open("File_Handling/municipios.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        return [city[2] for city in data if name in city[2]]

def ammount_of_cities_with_name(name: str): # Retorna QUANTAS cidades possuem uma palavra específica no nome
    with open("File_Handling/municipios.csv", "r") as file:
        data = file.readlines()
        data.pop(0)
        data = [line.strip().split(",") for line in data]

        return sum(1 for city in data if name in city[2])

def menu():
    print("""Escolha uma opção:
1 - Pesquisar por estado
2 - Pesquisar por UF
3 - Ver códigos dos estados
4 - Ver estado com nome mais curto
5 - Ver estado com nome mais longo
6 - Ver quantas cidades possui um estado
7 - Ver quais cidades possuem determinado nome
8 - Ver quantas cidades possuem determinado nome
0 - Sair
-------------------------------------------------""")

def main():
    while True:
        menu()
        op = int(input("-> "))
        print()

        if op == 1:
            search = input("Insira um estado do Brasil: ")
            uf = find_uf(search)
            if uf != None:
                print(f"A UF de {search} é {uf}\n")
            else:
                print("Estado não encontrado na base de dados\n")

        elif op == 2:
            search = input("Insira uma UF: ")
            state = find_state(search)
            if state != None:
                print(f"{search} pertence à {state}\n")
            else:
                print("UF não encontrada na base de dados\n")

        elif op == 3:
            for state in get_state_codes():
                print(f"{state[0]} - {state[1]}")
            print()

        elif op == 4:
            print(f"O estado do Brasil com nome mais curto é o {shortest_state()}\n")

        elif op == 5:
            print(f"O estado do Brasil com nome mais longo é o {longest_state()}\n")

        elif op == 6:
            code = input("Insira o código de um estado: ")
            state = find_state_by_code(code)
            if state != None:
                print(f"{state} possui {cities_from_state(code)} cidades\n")
            else:
                print("Código não encontrado na base de dados\n")

        elif op == 7:
            name = input("Pesquisar cidades que possuem: ")
            cities = cities_with_name(name)

            if len(cities) == 0:
                print(f"Nenhuma cidade do Brasil possui {name} no nome\n")
            else:
                print("\n".join(sorted(cities)))
                print()

        elif op == 8:
            name = input("Pesquisar cidades que possuem: ")
            print(f"Existem {ammount_of_cities_with_name(name)} cidades com {name} no nome\n")

        elif op == 0:
            break

        else:
            print("Opção inválida!\n")


main()