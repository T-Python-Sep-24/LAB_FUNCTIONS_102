def splitString(phrase: str) -> str:
    """
    Separates the word at any capital letter and replace it with a small letter

    Args:
        phrase (str): Text in camelCase that is not seperated 

    Returns:
        str: new modified string splited by any cabital letter
    """

    if type(phrase) != str:
        return "The function parameter should only be a string"
    
    newString: str = ""
    for i in phrase:
        if i.isupper():
            newString += f" {i.lower()}"
        else:
            newString += i

    return newString

# call the function
result = splitString("helloWorldThere")
print(result)