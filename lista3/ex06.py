especial = False
maiusc = False
minusc = False
num = False

senha = input("Digite a senha: ")

for i in senha:
    if i in "!#$%&()*+,-./:;<=>?@[\]^_`{|}~":
        especial = True
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        maiusc = True
    elif i in "abcdefghijklmnopqrstuvwxyz":
        minusc = True
    elif i in "0123456789":
        num = True

if minusc and maiusc and num and especial:
    print("Senha forte")
elif minusc and num and especial and not maiusc:
    print("Senha média")
else:
    print("Senha fraca")