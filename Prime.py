def find_primes(start:int,end:int):
    '''This function finds the Prime number between the valuse that the user puts
    
    Args:
        start:int takes the start of the numbers that the user want to check
        end:int   take the end of the numbers that teh user want to check
    returns:
            the function prints the values of the prime numbers between the start and the end
    
    '''
    for number in range(start,end+1): # end+1 to include the last number
        if number<=1:
            continue
        for i in range(2,number):
            if number % i==0:
                break
        else:
            print(number)

start=int(input("Choose a starting number: "))
end=int(input("Choose an ending number: "))

find_primes(start,end)
