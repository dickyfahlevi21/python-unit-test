'''Trim Word'''
import unittest

def trim_text(text:str, len_text:int):
    if type(text) != str or type(len_text) != int:
        raise ValueError
    trim = ' '.join(text.split(" ")[:len_text])
    return trim

# print(trim_text("satu dua tiga empat lima", 2))