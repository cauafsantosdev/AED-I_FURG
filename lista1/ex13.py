n = int(input("Digite um número: "))
c = 0
t = 1

print()

while c <= n:
	print(f"Tabuada do {c}:")
	while t <= 10:
		print(f"{c} x {t} = {c * t}")
		t = t + 1
	
	t = 0
	c = c + 1
	print()
		
