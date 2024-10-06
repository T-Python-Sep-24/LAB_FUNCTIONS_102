def find_primes(start: int, end: int) -> None:
    """Prints prime numbers between start and end (inclusive)."""
    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    break
            else:
                print(number)

def separate_camel_case(s: str) -> str:
    """Separates words in a camel case string and returns a modified string."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    result = []
    word = []

    for char in s:
        if char.isupper() and word:
            result.append(''.join(word).lower())
            word = []
        word.append(char)

    result.append(''.join(word).lower())  # Add the last word
    return ' '.join(result)


print("Prime numbers between 25 and 50:")
find_primes(25, 50)

modified_string = separate_camel_case("helloWorldThere")
print(f"Modified string: {modified_string}")
