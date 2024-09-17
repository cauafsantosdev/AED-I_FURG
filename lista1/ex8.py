t1 = str(input("Time 1: "))
t2 = str(input("Time 2: "))
t3 = str(input("Time 3: "))
t4 = str(input("Time 4: "))

g1, g2 = input(f"\nResultado da semifinal {t1} x {t2}: ").split("x")
g1 = int(g1)
g2 = int(g2)

if g1 > g2:
    f1 = t1
else:
    if g2 > g1:
        f1 = t2
    else:
        while True:
            p1, p2 = input(f"Resultado dos pênaltis {t1} x {t2}: ").split("x")
            p1 = int(p1)
            p2 = int(p2)
            
            if p1 == p2:
                print("Resultado inválido, insira novamente.\n")
            else:
                if  p1 > p2:
                    f1 = t1
                else:
                    f1 = t2
                break
                
g3, g4 = input(f"\nResultado da semifinal {t3} x {t4}: ").split("x")
g3 = int(g3)
g4 = int(g4)
                
if g3 > g4:
    f2 = t3
else:
    if g4 > g3:
        f2 = t4
    else:
        while True:
            p3, p4 = input(f"Resultado dos pênaltis {t3} x {t4}: ").split("x")
            p3 = int(p3)
            p4 = int(p4)
            
            if p3 == p4:
                print("Resultado inválido, insira novamente.\n")
            else:
                if  p3 > p4:
                    f2 = t3
                else:
                    f2 = t4
                break
                
print(f"\n{f1} e {f2} avançam para a final")
                
gf1, gf2 = input(f"\nResultado da final {f1} x {f2}: ").split("x")
gf1 = int(gf1)
gf2 = int(gf2)

if gf1 > gf2:
    print(f"\n{f1} foi o campeão!")
else:
    if gf2 > gf1:
        print(f"\n{f2} foi o campeão!")
    else:
        while True:
            pf1, pf2 = input(f"Resultado dos pênaltis {f1} x {f2}: ").split("x")
            pf1 = int(pf1)
            pf2 = int(pf2)
            
            if pf1 == pf2:
                print("Resultado inválido, insira novamente.\n")
            else:
                if  pf1 > pf2:
                    print(f"\n{f1} foi o campeão!")
                else:
                    print(f"\n{f2} foi o campeão!")
                break
