
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


def findPrimes(num1:int, num2: int):
    """
        This function finds the prime numbers between any two numbers provided by the user
    """
    for i in range(num1, num2 + 1):

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


findPrimes(number1, number2)