def find_primes(num1:int , num2:int):

    for number in range(num1 , num2+1):
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                break
        else:
            print(number)




find_primes(25, 50)