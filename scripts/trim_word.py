'''Trim Word'''
import unittest

def trim_text(text:str, len:int):
    if type(text) != str or type(len) != int:
        raise ValueError
    trim = ' '.join(text.split(" ")[:len])
    return trim

# print(trim_text("satu dua tiga empat lima", 2))