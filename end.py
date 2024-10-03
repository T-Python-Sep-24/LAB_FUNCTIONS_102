def mod_str(str1:str)->str:
    if not isinstance(str1,str):
        raise TypeError("not a string")
    mod_str = ''
    for char in str1:
        if char.isupper() and mod_str:
            mod_str += ' '
        mod_str += char.lower()
    return mod_str
result = mod_str("helloWorldThere")
print(result)