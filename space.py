def seprate_word (phrase:str)->str:
    '''
    Separates words in a string at capital letters and converts them to lowercase.
    args: 
        Pharse/String:str it takes the string that the function will work on
    return:
        a string with the new results
      
    '''
    if not isinstance(phrase,str):
        print("This program only accepts String values")
        print(type(phrase))
        exit()
    result=""
    for c in phrase:
        if c.isupper():
            result +=" "+c.lower()
        else:
            result +=c
    return result.strip()

print(seprate_word("HelloWorldThere"))