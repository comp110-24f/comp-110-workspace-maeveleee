"""Unit test for find_max"""
__author__ = "730824450"

from CQs.cq07.find_max import find_and_remove_max

def test_find_and_remove_max() -> None:
    #testing to see if the function returns the max value
    a = [5, 9, 6, 9]
    assert find_and_remove_max(a) == 9

def test_input_mutation_expected() -> None:
    #testing to see if the function deletes the max values
    a = [5, 9, 7, 8, 9]
    find_and_remove_max(a)
    assert a == [5, 7, 8]


def test_empty_list() -> None:
    #testing to see if the fuction returns -1 for empty lists
    a = []
    assert find_and_remove_max(a) == -1
