def separateStrings(input_string:str):
    if type(input_string) != str:
        return 'Input is not a string'

    output_string = ''
    flag = False  
    
    for char in input_string:
        if char.isupper():  
            if flag:  
                output_string += " "
                
            output_string += char.lower() 
            flag = True
        else:
            output_string += char 
            flag = True 

    return output_string  

print(separateStrings("helloWorldThere"))  