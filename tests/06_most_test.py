import unittest
import sys
sys.path.append('./scripts/')
from most_frequent import mode_freq



class TestLeap(unittest.TestCase):
    
    # Positive Test Freq is mode
    def test_is_mode(self):
        self.assertEqual(mode_freq([1,2,3,4,5,6,6,8,8,6,9]), 6, msg="Test Case is mode")

    # Negative Test Freq is not mode
    def test_is_not_mode(self):
        self.assertNotEqual(mode_freq([1,2,3,4,5,6,6,8,8,6,9]), 5, msg="Test Case is not mode")

    # Negative Test Freq is not List
    def text_is_not_str(self):
        self.assertRaises(ValueError, mode_freq("1"), "5")


if __name__ == "__main__":
    unittest.main()