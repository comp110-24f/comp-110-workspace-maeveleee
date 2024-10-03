"""returns the concatenation of the two input strings"""

__author__ = "730824450"

def concat(word1 : str, word2 : str) -> str:
    return word1 + word2

word1 = "happy"
word2 = "tuesday"
#as word1 and word2 are global variables, 
#they should be assigned outside the definition

if __name__ == "__main__":
    print(concat(word1, word2))