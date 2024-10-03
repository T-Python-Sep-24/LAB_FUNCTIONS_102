def fun1(sentence:str) :
    if not isinstance(sentence, str):
        print("sentence must be a string")
    
    result = ''
    for char in sentence:
        if char.isupper():
            result += ' ' + char.lower()
        else:
            result += char
    return result
result = fun1("helloWorldThere")
print(result)  