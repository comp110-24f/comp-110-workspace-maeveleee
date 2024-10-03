"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730824450"

def main() -> None:
    contains_char(word = input_word(), letter = input_letter())

def input_word() -> str:
    """entering the word"""
    word : str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """entering the letter"""
    letter : str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word : str, letter : str) -> None:
    print("Searching for " + letter + " in " + word)
    #spaces between front and back of in
    count : int = 0
    #as while loop cannot be used in this case
    #we need to write if statements for every scenario 
    #where the letter exists in the word
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        if count == 1:
            print(str(count) + " instance of " + letter + " found in " + word)
        else:
            print(str(count) + " instances of " + letter + " found in " + word)
            #we need to consider cases where there's a single instance or more than one


if __name__ == "__main__":
    main()