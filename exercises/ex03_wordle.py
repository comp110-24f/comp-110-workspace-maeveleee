"""EX03 - Wordle! Simple yet an interactive game"""

__author__ = "730824450"

def input_guess(secret_word_len : int) -> str:
    """entering the word with the correct length"""
    guess : str = input(f"Enter a {secret_word_len} character word: ")
    #we start by getting the input for guess
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess

def contains_char(search : str, char : str) -> bool:
    """testing if the characters match!"""
    #search is the secret word and char is a character in the guess
    #as long as there exists a char in search, we get TRUE
    assert len(char) == 1
    i = 0
    while i < len(search):
        if search[i] == char:
            return True
        i += 1
    return False

def emojified(guess : str, secret_word : str) -> str:
    """print color-coded emojis based on the matches"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result : str = ""
    i = 0
    while i < len(guess):
        #we will be searching if the character in guess exists in the secret word
        if contains_char(search = secret_word[i], char = guess[i]):
            result += GREEN_BOX #exact match
        elif contains_char(search = secret_word, char = guess[i]):
            result += YELLOW_BOX #exists but wrong position
        else:
            result += WHITE_BOX #doesn't exist
        i += 1
    return result
        
def main(secret_word : str) -> None:
    """This is the main function for Wordle!"""
    i = 1
    secret_word_len = len(secret_word)
    while i <= 6:
        print(f"== Turn {i}/6 ==")
        guess = input_guess(secret_word_len)
        print(emojified(guess, secret_word))
        if guess != secret_word:
            #when the guess is wrong
            i += 1
        elif guess == secret_word:
            #when the guess is correct
            print(f"You won in {i}/6 turns!")
            i = 8
            #so that we can differentiate correct guess from the wrong   
    if i == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main( secret_word = "codes" )

            
        


        




