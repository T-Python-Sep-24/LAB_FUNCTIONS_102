def find_primes(start: int, end: int):
    '''
    function finds and prints all prime numbers between the two integers.
    
    '''
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

find_primes(25, 50)
