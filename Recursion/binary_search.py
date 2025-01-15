def binary_search(n: int, search: list):
    idx = len(search) // 2

    if search[idx] == n:
        return n
    
    if search[idx] > n:
        print("bigger")
        return binary_search(n, search[:idx])
    
    if search[idx] < n:
        print("smaller")
        return binary_search(n, search[idx:])
    

print(binary_search(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))