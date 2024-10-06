def find_primes(n1: int, n2: int):
    """
    print the prime numbers between the first parameter and the second parameter

    Args:
        n1 (int): first parameter
        n2 (int): second parameter

    Returns:
        None: this function does not return any value
    """
    print("start")
    for i in range(n1, n2+1):
        isPrime = True
        # loop throgh numbers and check if it's divisible by other than itself 
        for j in range(2, n2):
            if j == i:
                continue
            elif i % j == 0:
                isPrime = False
                break

        if isPrime:
            print(i)
        
find_primes(25, 50)