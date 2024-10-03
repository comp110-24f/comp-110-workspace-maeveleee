"""practice using a while loop"""
__author__ = "730824450"

def num_instances(phrase : str, search_char : str) -> int:
    count : int = 0
    index : int = 0
    while index < len(phrase):
        #runs while loop as many as the length of the phrase
        if phrase[index] == search_char:
            count = count + 1
            #if there is the character we're looking for on phrase[index]
        index = index + 1
        #index should be increased after the if statement 
        #so that we would be starting checking phrase[index]
        #from the first character
    return count