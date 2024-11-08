def define_lang(people: int):
    languages = []

    for i in range(people):
        lang = input("")
        languages.append(lang)

    for language in languages:
        if language != languages[0]:
            return "ingles"
        
    return languages[0]


cases = int(input(""))

for i in range(cases):
    people = int(input(""))
    print(define_lang(people))