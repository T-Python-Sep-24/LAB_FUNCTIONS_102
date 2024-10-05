def find_primes(start: int, end: int):
    for num in range(start, end + 1):  # Loop through numbers between start and end
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True  # Assume the number is prime
            for i in range(2, num):  # Check divisibility from 2 up to the number itself
                if num % i == 0:  # If divisible by any number, it's not prime
                    is_prime = False
                    break  # Stop checking if not prime
            if is_prime:
                print(num)  # Print the prime number

find_primes(25, 50)