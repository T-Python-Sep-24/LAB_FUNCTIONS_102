#Function that finds primes 
def find_primes(num1:int, num2: int):
    '''
    This function takes in 2 parameters of type int, and prints the prime numbers between the first parameter and the second parameter
    '''
    #Creating the range of numbers 
    numbers = range(num1, num2 + 1)
    for number in numbers:
        #Number has to be greater than 1 and a positive 
        if number > 1:
            for i in range(2, number):
                #If number is divisible by 2 or any other number in the range it's not a prime
                if (number % i) == 0:
                    break
            else: 
                print(number)

#Asking user for a range of numbers
print("--- Finding prime numbers in a range ---")
number1: int = int(input("Please enter the first number in the range: "))
number2: int = int(input("Please enter the last number in the range: "))

#Calling the function with the range the user chose
find_primes(number1, number2)
