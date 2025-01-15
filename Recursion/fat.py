def fat(n: int):
    if n == 1:
        return 1
    
    return n * fat(n-1)


print(fat(4))
print(fat(5))
print(fat(6))