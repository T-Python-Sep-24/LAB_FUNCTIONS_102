#Defining a function that takes string as a parameter then modifies it
def modifyStr(phrase: str) -> str:
    '''
    This function recieves a string as a parameter,
    then separates the words at every upper letter and replacing it with a lower

    Args:
        phrase: The string to be modified 
    Returns:
        Modified string; same string but separating the word that start with an upper,
        and replacing the uppe with a lower
    '''
    modifiedPhrase: str = ""

    if isinstance(phrase, str):
        for letter in phrase:
            if letter.isupper():
                modifiedPhrase += f" {letter.lower()}"
                continue
            modifiedPhrase += letter
        return modifiedPhrase
    else: 
        return "This is not a string!"
    
#Invoking function with the desired phrase
print(modifyStr("helloBeautifulPeopleHowAreYou"))