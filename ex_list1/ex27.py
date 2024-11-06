t = input("Informe o tijolo: ")
a = int(input("Informe a quantidade de andares: "))
n = 0

while n < a:
	n += 1
	e -= 1
	c = 0

	while e >= n:
		print(end=" ")
		e -= 1

	while c < (2 * n - 1):
		print(t, end="")
		c += 1
		
	print()
