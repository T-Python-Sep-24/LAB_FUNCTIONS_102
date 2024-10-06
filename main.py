def find_primes(a, b):
    for number in range(a, b):

        if n > 1:
            is_prime = True


            for i in range(2, n):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(n)
find_primes(3, 10)







