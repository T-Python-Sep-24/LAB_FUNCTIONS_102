## Create a function : find_primes that takes in 2 parameters of type int , 
# and print the prime numbers between the first parameter and the second parameter . 

def find_primes(start: int, end: int):
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)

# primes between `25` and `50` are:
find_primes(25, 50)