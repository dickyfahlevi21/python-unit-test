import unittest
import sys
sys.path.append('./scripts/')
from trim_word import trim_text



class TestLeap(unittest.TestCase):
    
    # Positive Test is trim
    def test_is_trim(self):
        self.assertEqual(trim_text("ini adalah tulisan yang sangat panjang", 3), "ini adalah tulisan", msg="Test Case is trim")

    # Negative Test is not trim
    def test_is_not_trim(self):
        self.assertNotEqual(trim_text("ini adalah tulisan yang sangat panjang", 3), "ini adalah tulisan panjang", msg="Test Case is not trim")

    # # Negative Test Text is not String
    # def text_is_not_str(self):
    #     self.assertRaises(ValueError, trim_text(2, 3), '2')

    # # Negative Test Len is not Integer
    # def text_is_not_int(self):
    #     self.assertRaises(ValueError, trim_text("ini adalah tulisan panjang", '3'), 2)


if __name__ == "__main__":
    unittest.main()