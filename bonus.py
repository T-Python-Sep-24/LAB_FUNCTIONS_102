'''
# Bonus
'''

def string_seprator(statement:int)->str:
    '''
    separates a statement at capital letters.

    Args:
        statement (str): An input string.

    Returns:
        new_statement (str): A modified statement.
        str: If the argument is not a string returns "your input is not a string".
    '''
    new_statement=""
    if type(statement)==type("str"):
        for i in statement:
            if not i.islower():
                new_statement+= ' '+i.lower()
            else:
                new_statement+= i
        return new_statement        
    else:
        return "your input is not a string"


print(string_seprator("helloWorldThere"))