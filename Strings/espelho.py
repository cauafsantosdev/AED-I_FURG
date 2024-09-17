x = input("Digite seu nome: ")
n = x.split()
t = len(n)
c = 0

while c < t:
	i = len(n[c])
	while i > 0:
		print(n[c][i - 1], end="")
		i -= 1
	print(end=" ")
	c += 1

print()	
