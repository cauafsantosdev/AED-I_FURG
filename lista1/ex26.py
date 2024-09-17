m = 0
s = 0

while s <= 60:
    if s < 10:
        print(f"{m}:0{s}")
        s += 1
    if s >= 10:
        print(f"{m}:{s}")
        s += 1
    if s == 60:
        m += 1
        s = 0
        if m == 10:
            print(f"{m}:0{s}")
            s = 61
