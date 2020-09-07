'''Character Length'''
import unittest



def char_len(val:str):
    if type(val) is not str:
        raise ValueError
    return len(val)