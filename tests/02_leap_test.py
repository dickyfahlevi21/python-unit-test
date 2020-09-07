import unittest
import sys
sys.path.append('./scripts/')
from leap_year import is_leap



class TestLeap(unittest.TestCase):
    
    # Positive Test is Leap Year
    def test_is_leap(self):
        self.assertEqual(is_leap(2004), "Kabisat", msg="Test Case is Leap Year")

    # Negative Test is not Leap Year
    def test_is_not_leap(self):
        self.assertEqual(is_leap(2001), "Bukan Kabisat", msg="Test Case is not Leap Year")

    # Negative Test Error is String
    def test_is_not_int(self):
        self.assertRaises(ValueError, is_leap, '2')


if __name__ == "__main__":
    unittest.main()