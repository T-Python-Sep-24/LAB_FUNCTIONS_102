'''
# LAB_FUNCTIONS_102

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between `25` and `50` are:
```
29   
31   
37   
41   
43   
47   
```



'''
def find_primes(x:int,y:int):
   if x<=1:
      print("your numbers range starts with a non prime number")
      return
   for j in range(x,y+1):
    is_prime = True
    for i in range(2,int(j**0.5)+1):
            if  j%i==0 :
                is_prime = False
                break
    if is_prime:        
        print(j)




find_primes(25,50)

