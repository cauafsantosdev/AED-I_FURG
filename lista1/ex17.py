n = int(input("Determine a quantidade de termos da sequência: "))
t0 = 0
t1 = 1
c = 0
 
while c <= n:
    c += 1
    f = t0 + t1
    print(t0, end=' -> ' if c <= n else '\n')
    t0 = t1
    t1 = f
