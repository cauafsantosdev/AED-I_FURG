t = input("Informe o tijolo: ")
a = int(input("Informe a quantidade de andares: "))
n = 0

# Piramide com while    
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
	
print()

# Piramide invertida com while

n = a

while n > 0:
	e = a - n
	c = 0

	while e > 0:
		print(end=" ")
		e -= 1

	while c < (2 * n - 1):
		print(t, end="")
		c += 1
	
	n = n - 1
	print()

print()

# Piramide com for
for i in range(1, a + 1):
    for j in range(1, (a - i) + 1):
        print(end=" ")
    
    while n != (2 * i - 1):
        print(t, end="")
        n = n + 1
    
    n = 0
    print()
    
print()

# Piramide invertida com for
for i in range(a, 0, -1):
    for j in range(1, (a - i) + 1):
        print(end=" ")
    
    while n != (2 * i - 1):
        print(t, end="")
        n = n + 1
    
    n = 0
    print()
