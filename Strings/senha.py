especial = False
maiusc = False
minusc = False
num = False

senha = input("Digite a senha: ")

if len(senha) >= 8:
    forca = 1
else:
    forca = 0

for i in senha:
    if i in "!#$%&()*+,-./:;<=>?@[\]^_`{|}~":
        especial = True
    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        maiusc = True
    elif i in "abcdefghijklmnopqrstuvwxyz":
        minusc = True
    elif i in "0123456789":
        num = True

if especial:
    forca += 1
if maiusc:
    forca += 1
if minusc:
    forca += 1
if num:
    forca += 1

if forca <= 2:
    print("Senha fraca")
elif forca <= 4:
    print("Senha média")
else:
    print("Senha forte")