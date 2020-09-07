'''Convert Number'''
import unittest



def number_to_string(n):
    numbers = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    result = " "
    number = int(n)

    if type(n) is not int:
        raise ValueError
    if number >= 0 and number <= 11:
        result = numbers[number]
    elif n < 20:
        result = number_to_string (number - 10) + " Belas "
    elif n < 100:
        result = number_to_string (number / 10) + " Puluh " + number_to_string (number % 10)
    return result