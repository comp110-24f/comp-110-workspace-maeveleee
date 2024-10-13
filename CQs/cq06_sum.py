"""Summing the elements of a list using different loops"""
__author__ = "730824450"

def w_sum(vals : list[float]) -> float:
    i = 1
    sum : float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum

def f_sum(vals : list[float]) -> float:
    sum : float = 0.0
    #initialize a variable
    for elem in vals:
        sum += elem
    return sum

def f_range_sum(vals : list[float], start, end) -> float:
    #set the range as start and end
    sum : float = 0.0
    for elem in range(start, end):
        # range is inside the for loop
        sum += elem
    return sum


