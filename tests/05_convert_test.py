import unittest
import sys
sys.path.append('./scripts/')
from convert_number import number_to_string



class TestLeap(unittest.TestCase):
    
    # Positive Test Convert is convert
    def test_is_convert(self):
        self.assertEqual(number_to_string(1), "Satu", msg="Test Case is convert")

    # Negative Test Convert is not convert
    def test_is_not_convert(self):
        self.assertNotEqual(number_to_string(1), "Dua", msg="Test Case is not convert")

    # Negative Test Convert is not Int
    def text_is_not_str(self):
        self.assertRaises(ValueError, number_to_string("1"), "Dua")


if __name__ == "__main__":
    unittest.main()