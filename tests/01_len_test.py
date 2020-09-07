import unittest
import sys
sys.path.append('./scripts/')
import len_char



class TestLen(unittest.TestCase):
    
    # Positive Test is Equal char with length
    def test_is_equal(self):
        self.assertEqual(len_char.char_len('saya'), 4, msg="Test Case is Equal")

    # Negative Test is not Equal char with length
    def test_is_not_equal(self):
        self.assertNotEqual(len_char.char_len('saya'), 5, msg="Test Case is not Equal")

    # Negative Test is not String
    def test_is_not_str(self):
        self.assertRaises(ValueError, len_char.char_len, 2)


if __name__ == "__main__":
    unittest.main()