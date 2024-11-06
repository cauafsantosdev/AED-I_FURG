n = float(input("Digite um número: "))
#rq = n ** (.5)
r = n / 2
rq = r * r

while rq > n:
	r /= 2
	rq = r * r

while rq < n:
	r += 0.00001
	rq = r * r

if n == int(n):
	print(f"A raiz quadrada de {n:.0f} é {r:.4f}")
else:
	print(f"A raiz quadrada de {n} é {r:.4f}")
