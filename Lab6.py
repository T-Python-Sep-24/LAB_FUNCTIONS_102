#Lab 6

#The answer
def myPrimes(x:int, y:int):
    """
    This function takes two integers, `x` and `y`, and prints all the prime numbers between them (inclusive).
    
    Args:
    x (int): The starting number of the range.
    y (int): The ending number of the range.
    """

    def checkPrimes(n: int):
        """
        This helper function checks if a given number `n` is prime.
        """
        if n <=1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
             return False
        return True
    
    # Iterate over the range from start to end and print prime numbers
    for num in range(x, y + 1):
        if checkPrimes(num):
            print(num)

# Example usage
myPrimes(10, 50)
