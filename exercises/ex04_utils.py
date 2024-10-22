"""EX04 - Wordle! Simple yet an interactive game"""

__author__ = "730824450"

def all(list1 : list[int], int1 : int) -> bool:
    if len(list1) == 0:  
        return False
    #return False when the list is empty
    
    i = 0
    while i < len(list1):
        if list1[i] != int1:
            return False
            #exits the loop
        i += 1
    return True

def max(list1 : list[int]) -> int:
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")
        #raise an error when the list in empty
    
    max_num : int = list1[0]
    #instead of assigning it to 0, it counts for negative numbers
    for elem in list1:
        if elem > max_num:
            max_num = elem

    return max_num
    #return the maximum number in the list if found
    #otherwise raise error

def is_equal(list1 : list[int], list2 : list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    #exit the loop before entering

    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            return False
        #exit if at least one index doesn't align
        i += 1
    
    return True

def extend(list1 : list[int], list2 : list[int]) -> None:
    for elem in list2:
        list1.append(elem)
        #add all the elements from list2 to list1    

    