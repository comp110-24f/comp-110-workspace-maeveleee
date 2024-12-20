"""List Utility Functions"""
__author__ = "730824450"

def only_evens(list1 : list[int]) -> list[int]:
    #creates a new list with only even numbers
    list2 : list[int] = []
    i = 0
    while i < len(list1):
        if list1[i] % 2 == 0:
            list2.append(list1[i])
        i += 1
    return list2

def sub(list1 : list[int], start : int, end: int) -> list[int]:
    #generates the subset of the list
    if len(list1) == 0 or start >= len(list1) or end <= 0 or start >= end:
        return []
    #when the length of the list is zero or the range doesn't align,
    #it returns an empty set
    
    if start < 0:
        start = 0
    if end > len(list1):
        end = len(list1) 
    #adjusting the range of the list
    
    list2 : list[int] = []
    for i in range(start, end):
        list2.append(list1[i])

    return list2
    

def add_at_index(list1 : list[int], elem : int, ind : int) -> None:
    if ind < 0 or ind > len(list1):
        raise IndexError("Index is out of bounds for the input list")

    list1.append(0)

    for i in range(len(list1) - 1, ind, -1):
        list1[i] = list1[i - 1]
    
    list1[ind] = elem
    #adding elem at certain index of the list