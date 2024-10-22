"""Find the maximum numbers and delete them"""
__author__ = "730824450"

def find_and_remove_max(a : list[int]) -> int:
    if len(a) == 0:
        return -1
    #return -1 for empty lists
    
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    #find the maximum number from the list

    i = 0
    while i < len(a):
        if a[i] == max:
            a.pop(i)
        else:
            i += 1
    #delete the maximum numbers from the list
    
    return max



