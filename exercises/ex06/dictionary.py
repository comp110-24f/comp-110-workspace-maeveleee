"""Dictionary Utility Functions"""
__author__ = "730824450"

def invert(dict : dict[str, str]) -> dict[str, str]:
    inverted = {}
    for key in dict:
        #all the keys in dict
        value = dict[key]
        #all the values in dict
        if value in inverted:
            raise KeyError(f"Duplicate key {value} is found")
        #if value is already in inverted
        inverted[value] = key
    return inverted

def favorite_color(dict : dict[str, str]) -> str:
    count = {}

    for key in dict:
        value = dict[key]
        if value in count:
            count[value] += 1
        #adding 1 if it appears again
        else:
            count[value] = 1
        #assigning 1 if it appears for the first time

    max_value = ""
    max_num = 0
    
    for value in count: 
        num = count[value]
        if num > max_num:
            max_value = value
            max_num = num
        elif num == max_num:
            max_value = max_value

    return max_value

def count(list : list[str]) -> dict[str, int]:
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
            #increase by one if it's already there
        else:
            dict[item] = 1
            #initial count
    return dict

def alphabetizer(list : list[str]) -> dict[str, list[str]]:
    result = {}
    for elem in list:
        first = elem[0].lower()
        #first character of the word
        if first not in result:
            result[first] = []
        #if first character doesn't exist in result
        result[first].append(elem)
    return result

def update_attendance(attendance_log : dict[str, list[str]], day : str, student : str) -> None:
    #adding student to a day in a week
    if day in attendance_log:
        attendance_log[day].append(student) 
    else:
        attendance_log[day] = [student]