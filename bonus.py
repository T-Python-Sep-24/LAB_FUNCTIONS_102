def separate_words(input_string):
    
    # Check if the input is of type 'str'
    if type(input_string) != str:
        return "The input is not a string!"
    # Initialize an empty string to build the modified string
    modified_string = ""  
    # Loop through each character in the input string
    for char in input_string:  
        if char.isupper():  # If the character is uppercase
            # Add a space and the lowercase version of the letter
            modified_string += " " + char.lower() 
        else:
            modified_string += char  # If it's not uppercase, add it as it is
    # Return the modified string without leading or trailing spaces
    return modified_string.strip()  


result = separate_words("helloWorldThere")
print(result)  
