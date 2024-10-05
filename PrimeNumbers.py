def find_primes(x:int, y:int):
    '''This function prints the prime numbers between the first and the second parameter'''
    for num in range(x, y):
        flag = True
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                flag = False
                break
        if flag:
            print(num)
            
find_primes(25, 50)