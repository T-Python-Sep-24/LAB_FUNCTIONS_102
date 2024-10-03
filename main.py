#LAB_FUNCTIONS_102
def print_primes(start: int , end:int):
    for num in range(start, end +1):
        if (start == end):
            break
        else:
            if num > 1:
                for i in range(2 , num):
                    if (num % i ) == 0:
                        break
                else:
                    print(num)

print_primes(25,50)

#Bouns
def lower_strings(i: str):
    if not isinstance(i,str):
        return"Please enter strings"
    else:
        lowstr = ""
        for char in i:
            if char.isupper():
                lowstr += " " + char.lower()
            else:
                lowstr += char

        print(lowstr)
    
lower_strings("helloWorldThere")


