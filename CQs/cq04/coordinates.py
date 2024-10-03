"""print the formatted pairs of each character in the two input strings"""

__author__ = "730824450"

def get_coords(xs : str, ys : str) -> None:
    i = 0
    while i < len(xs):
        j = 0
        #we have to assign j=0 inside the outer loop
        #so that inner loop would be run for each digit of xs
        while j < len(ys):
            print("(" + str(xs[i]) + "," + str(ys[j]) + ")")
            j += 1
        i += 1
        #i is going to be increased by one in the end of the 
        #outer loop so that every digit would be counted
    return None
