from prime import fh


def prime_check(n: int):
    limit = int(n**0.5)
    prime_list = fh.get_list(limit)

    for i in prime_list:
        if n % i == 0:
            return False
    
    biggest = fh.biggest_prime()
    if limit > biggest:
        advanced_check(n, limit, biggest)
    
    return True

def advanced_check(n: int, limit: int, biggest: int):
        for i in range(biggest+1, limit+1):
            if prime_check(i):
                 fh.add_prime(i)
            if n % i == 0:
                return False
            
        return True
            
def primes_between(start: int, end: int):
    prime_list = [i for i in range(start, end+1) if prime_check(i)]
    return prime_list

def next_prime():
    n = fh.biggest_prime() + 1
    
    while True:
        if prime_check(n):
            fh.add_prime(n)
            return n
        else:
            n += 1
