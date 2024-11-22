
def get_list(limit: int):
    with open("Prime_Nums_Challenge/prime_numbers.txt", "r") as primes:
        prime_list = [int(i) for i in primes if int(i) <= limit]
    
    return prime_list

def full_list():
    with open("Prime_Nums_Challenge/prime_numbers.txt", "r") as primes:
        full_list = [int(i) for i in primes]
    
    return full_list

def add_prime(n: int):
    with open("Prime_Nums_Challenge/prime_numbers.txt", "r") as primes:
        if str(n) not in primes:
            with open("Prime_Nums_Challenge/prime_numbers.txt", "a") as primes:
                primes.write(f"{n}\n")

def biggest_prime():
    return max(full_list())