def find_primes(start: int, end: int):
    
    for num in range(start, end + 1):
        if num > 1:  
            for i in range(2, num):
                if num % i == 0:
                    break   
            else:
                print(num)  

find_primes(25, 50)