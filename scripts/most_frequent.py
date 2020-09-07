'''Most Frequent'''
import unittest



def mode_freq(value):
    if type(value) is not list:
        raise ValueError
    return max(set(value), key = value.count)

# diambil nilai tertinggi
# max(set(value)) = numbers = 9
# max(set(value)) = grades = 90.5
# lalu diambil nilai yang paling banyaknya
