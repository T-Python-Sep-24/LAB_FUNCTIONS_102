#Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter .
#hint : a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11) Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers

def find_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
find_primes(25, 50)