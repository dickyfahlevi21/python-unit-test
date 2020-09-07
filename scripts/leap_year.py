'''Leap Year'''
import unittest



def is_leap(year:int):
    if type(year) is not int:
        raise ValueError
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Kabisat"
    elif year % 100 == 0:
        return "Bukan Kabisat"
    else:
        return "Bukan Kabisat"

