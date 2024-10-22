"""Testing List Utility Functions"""
__author__ = "730824450"

from exercises.ex05.utils import only_evens, sub, add_at_index

def test_only_evens_use1() -> None:
    #use case 1 for only_evens
    list1 = [1, 2, 3, 4, 5]
    assert only_evens(list1) == [2, 4]

def test_only_evens_use2() -> None:
    #use case 2 for only_evens
    list1 = [34209, 423, 334, 3234, 335]
    only_evens(list1)
    assert list1 == [334, 3234]

def test_only_evens_edge() -> None:
    #edge case for only_evens
    list1 = []
    assert only_evens(list1) == []

def test_sub_use1() -> None:
    #use case 1 for sub
    list1 = [1, 2, 3, 4, 5]
    start = 1
    end = 3
    assert sub(list1, start, end) == [2]

def test_sub_use2() -> None:
    #use case 2 for sub
    list1 = [1, 2, 3, 4, 5]
    start = -1
    end = 35
    sub(list1, start, end)
    assert list1 == [1, 2, 3, 4, 5]

def test_sub_edge1() -> None:
    #edge case 1 for sub
    #when start is greater than end
    list1 = [1, 2, 3, 4, 5]
    start = 4
    end = 1
    sub(list1, start, end)
    assert list1 == []

def test_sub_edge2() -> None:
    #edge case 2 for sub when it's an empty set
    list1 = []
    start = 2
    end = 3
    assert sub(list1, start, end) == []

def test_add_at_index_use1() -> None:
    #use case 1 for add_at_index
    list1 = [1, 2, 3, 4, 5]
    elem = 1
    ind = 3
    assert add_at_index(list1, elem, ind) == [1, 2, 3, 1, 4, 5]

def test_add_at_index_use2() -> None:
    #use case 2 for add_at_index
    list1 = [1, 2, 3, 4, 5]
    elem = 7
    ind = 5
    add_at_index(list1, elem, ind)
    assert list1 == [1, 2, 3, 4, 5, 7]

import pytest

def test_add_at_index_edge1() -> None:
    #edge case 1 for add_at_index
    list1 = [1, 2, 3, 4, 5]
    elem = 6
    ind = 477
    with pytest.raises(IndexError):
        add_at_index(list1, elem, ind)