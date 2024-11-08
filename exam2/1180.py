size = int(input())
values = input().split()
values = [int(n) for n in values]

print(f"Menor valor: {min(values)}\nPosição: {values.index(min(values))}")