def write_date(date: str, place: str):
    months = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 
              7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

    day, month, year = map(int, date.split("/"))

    return f"{place}, {day} de {months[month]} de {year}."


date = input("Insira data em formato DD/MM/AAAA: ")
place = input("Onde você está? ")

print(f"\n{write_date(date, place)}")