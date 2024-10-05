#Bonus Lab 6

def myCapital(inputString):
    if not isinstance(inputString, str):
        return "Input is not a string"
    
    result = ''
    
    for char in inputString:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    
    return result.strip()


print(myCapital("helloWorldThere"))