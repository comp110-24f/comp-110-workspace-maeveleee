"""Mutating functions."""
__author__ = "730824450"

list_1 : list[int] = [1, 2, 3]
list_2 : list[int] = list_1

def manual_append(a : list[int], num : int) -> None:
    a.append(num)

def double(a : list[int]) -> None:
    i = 0
    while i < len(a):
        a[i] *= 2
        i += 1

double(list_2)
print(list_1)
print(list_2)