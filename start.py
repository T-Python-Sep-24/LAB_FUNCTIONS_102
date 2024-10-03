def check_prime(n:int)->bool:
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def find_prime(k:int, d:int):

    for number in range(k, d):
        if check_prime(number):
            print(number, end=' ')
    print()
find_prime(25, 50)
