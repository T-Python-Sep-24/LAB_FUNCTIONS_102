
def lower_strings(word: str):
    if not isinstance(word,str):
        return"Please enter strings"
    else:
        lowstr = ""
        for char in word:
            if char.isupper():
                lowstr += " " + char.lower()
            else:
                lowstr += char
        print(lowstr)


lower_strings("helloWorldThere")