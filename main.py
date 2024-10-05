firstNumber = int(input("Enter the first number:"))
endNumber = int(input("Enter the end numbers ")) 
def find_primes():
    '''
    Finds and prints all prime numbers within a specified range.
    This function uses two global variables, `firstNumber` and `endNumber`, to define the range.
    It iterates through all the numbers in this range, checks each number for primality, and prints the prime numbers.
    
    ''' 
    for primeNumber in range(firstNumber , endNumber):
            if primeNumber > 1  :
                for counterNumber in range (2, primeNumber):
                    if primeNumber % counterNumber == 0:
                         break
                else:
                    print(primeNumber)

find_primes ()