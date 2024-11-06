a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

if a > b > c or a == b > c:
        a, b, c = c, b, a
else:
	if a > c > b or a == c > b:
		a, b, c = b, c, a
	else:
		if b > c > a or b == c > a:
			a, b, c = a, c, b
		else:
			if b > a > c:
				a, b, c = c, a, b
			else:
				if c > a > b:
					a, b, c = b, a, c
				else:
					if c > b > a:
					    a, b, c = a, b, c

if a == int(a):
    print(int(a), end=' ')
else:
    print(a, end=' ')

if b == int(b):
    print(int(b), end=' ')
else:
    print(b, end=' ')

if c == int(c):
    print(int(c))
else:
    print(c)
