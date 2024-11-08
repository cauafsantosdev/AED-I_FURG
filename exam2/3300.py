def mala_suerte(number: str):
    if "13" in number:
        return f"{number} es de Mala Suerte"
    return f"{number} NO es de Mala Suerte"
        

number = input()
print(mala_suerte(number))