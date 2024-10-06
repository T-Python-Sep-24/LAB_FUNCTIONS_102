def formatting(sentence: str):
    new_sentence = ""

    for ch in sentence:
        if ch.isupper():
            new_sentence += " "
        new_sentence += ch
    return new_sentence

result = formatting("helloEyad")
print(result)
