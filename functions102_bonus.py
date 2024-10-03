
user_string = input("Enter your string \"with no spaces\": ")


def formater(user_str:str):
    """
        This function takes a string that may contain capital letters and not spaces,
        and Returns and well formatted string that has small letters and spaced properly
    """

    if user_str.isalpha():

        for letter in user_str:
            if letter.isupper():
                user_str = user_str.replace(letter, f" {letter.lower()}")

        return user_str
    else:
        print("Please Enter a STRING only \"with no spaces\"")


print(formater(user_string))
