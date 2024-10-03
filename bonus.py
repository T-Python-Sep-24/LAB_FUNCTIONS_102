def stringFunction (inputString):

    if not isinstance(inputString,str):
       print("the input should be a string!")
    
    outcome =" "
    for character in inputString :
        if character.isupper():
            outcome += " " + character.lower()
        else:
            outcome +=character
    return outcome
    
print(stringFunction("helloWorldThere"))




