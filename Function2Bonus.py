'''write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !'''

def modify_string(s: str) -> str:
    # Check if the parameter is of type str
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    # Use a list to collect modified characters
    modified_string = []
    
    for char in s:
        if char.isupper() and modified_string:  # If it's an uppercase letter and not the first character
            modified_string.append(' ')  # Add a space before it
        modified_string.append(char.lower())  # Append the lowercase version of the character
    
    return ''.join(modified_string)


result = modify_string("helloWorldThere")
print(result)  # Output: hello world there