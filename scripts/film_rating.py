'''Film Rating'''
import unittest

def check_rating(age:int):
    if type(age) is not int or age == 0:
        raise ValueError

    if age >= 21:
        return "DEWASA"
    elif age >= 13:
        return "REMAJA"
    elif age >= 9:
        return "BIMBINGAN ORANG TUA"
    elif age >= 1 or age <= 8:
        return "SEMUA USIA"
