def convert_bin(n: int):
    binary = []
    while n >= 1:
        binary.append(int(n % 2))
        n /= 2
    
    binary = "".join(map(str, reversed(binary)))
    return int(binary)


n = int(input("Digite um número: "))
binario = convert_bin(n)

print(f"{n} em binário é {binario}")