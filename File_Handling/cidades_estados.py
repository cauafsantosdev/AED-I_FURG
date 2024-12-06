class Country:
    def __init__(self):
        self.__states = []
        self.__cities = []

    def get_states(self, filename: str):
        with open(filename, "r") as file:
            data = file.readlines()
            data.pop(0)
            self.__states = [line.strip().split(",") for line in data]
    
    def get_cities(self, filename: str):
        with open(filename, "r") as file:
            data = file.readlines()
            data.pop(0)
            self.__cities = [line.strip().split(",") for line in data]

    def find_uf(self, search: str): # Procura a UF de um estado através do nome
        for state in self.__states:
            if state[1] == search:
                return state[2]

    def find_state(self, search: str): # Procura o nome de um estado através da UF
        for state in self.__states:
            if state[2] == search:
                return state[1]

    def get_state_codes(self, ): # Retorna os códigos dos estados segundo o IBGE
        return sorted([[state[0], state[1]] for state in self.__states])

    def find_state_by_code(self, code: str): # Procura o nome do estado através do código
        for state in self.__states:
            if state[0] == code:
                return state[1]

    def shortest_state(self, ): # Retorna o estado com nome mais curto
        return min(self.__states, key=lambda state: len(state[1]))[1]

    def longest_state(self, ): # Retorna o estado com nome mais longo
        return max(self.__states, key=lambda state: len(state[1]))[1]

    def cities_from_state(self, code: str): # Retorna o número de cidades de um determinado estado
        return sum(1 for city in self.__cities if city[0] == code)

    def cities_with_name(self, name: str): # Retorna AS cidades que possuem uma palavra específica no nome
        return [city[2] for city in self.__cities if name in city[2]]

    def ammount_of_cities_with_name(self, name: str): # Retorna QUANTAS cidades possuem uma palavra específica no nome
        return sum(1 for city in self.__cities if name in city[2])


class CountryApplication:
    def __init__(self):
        self.__country = Country()

    def menu(self):
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

    def main(self):
        self.__country.get_states("File_Handling/estados.csv")
        self.__country.get_cities("File_Handling/municipios.csv")

        while True:
            self.menu()
            op = int(input("-> "))
            print()

            if op == 1:
                search = input("Insira um estado do Brasil: ")
                uf = self.__country.find_uf(search)
                if uf != None:
                    print(f"A UF de {search} é {uf}\n")
                else:
                    print("Estado não encontrado na base de dados\n")

            elif op == 2:
                search = input("Insira uma UF: ")
                state = self.__country.find_state(search)
                if state != None:
                    print(f"{search} pertence à {state}\n")
                else:
                    print("UF não encontrada na base de dados\n")

            elif op == 3:
                for state in self.__country.get_state_codes():
                    print(f"{state[0]} - {state[1]}")
                print()

            elif op == 4:
                print(f"O estado do Brasil com nome mais curto é o {self.__country.shortest_state()}\n")

            elif op == 5:
                print(f"O estado do Brasil com nome mais longo é o {self.__country.longest_state()}\n")

            elif op == 6:
                code = input("Insira o código de um estado: ")
                state = self.__country.find_state_by_code(code)
                if state != None:
                    print(f"{state} possui {self.__country.cities_from_state(code)} cidades\n")
                else:
                    print("Código não encontrado na base de dados\n")

            elif op == 7:
                name = input("Pesquisar cidades que possuem: ")
                cities = self.__country.cities_with_name(name)

                if len(cities) == 0:
                    print(f"Nenhuma cidade do Brasil possui {name} no nome\n")
                else:
                    print("\n".join(sorted(cities)))
                    print()

            elif op == 8:
                name = input("Pesquisar cidades que possuem: ")
                print(f"Existem {self.__country.ammount_of_cities_with_name(name)} cidades com {name} no nome\n")

            elif op == 0:
                break

            else:
                print("Opção inválida!\n")


app = CountryApplication()
app.main()