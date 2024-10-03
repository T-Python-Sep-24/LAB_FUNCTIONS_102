
def find_primes(start:int, end:int):
    for number in range(start, end + 1): #end + 1 includes the end value since range is exclusive
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)

firstNumber = int(input("enter first number : "))
secondNumber = int(input("enter second number : "))

find_primes(firstNumber,secondNumber)
