def find_primes(par1: int, par2: int):
      
      for num in range(par1, par2 + 1):
        if num <= 1:
            continue  # Skip numbers less than or equal to 1
        is_prime = True # mark it is  a prime

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False # mark it is not a prime
                break

        if is_prime:
            print(num)

find_primes(25,50)