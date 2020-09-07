import unittest
import sys
sys.path.append('./scripts/')
from len_char import char_len



class TestLen(unittest.TestCase):
    
    # Positive Test is Equal char with length
    def test_is_equal(self):
        self.assertEqual(char_len('saya'), 4, msg="Test Case is Equal")

    # Negative Test is not Equal char with length
    def test_is_not_equal(self):
        self.assertNotEqual(char_len('saya'), 6, msg="Test Case is not Equal")

    # Negative Test is not String
    def test_is_not_str(self):
        self.assertRaises(ValueError, char_len, 2)


if __name__ == "__main__":
    unittest.main()