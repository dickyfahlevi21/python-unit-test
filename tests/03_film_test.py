import unittest
import sys
sys.path.append('./scripts/')
from film_rating import check_rating



class TestLeap(unittest.TestCase):
    
    # Positive Test is Rating
    def test_is_rating(self):
        self.assertEqual(check_rating(22), "DEWASA", msg="Test Case is Rating")

    # Negative Test is not Rating
    def test_is_not_rating(self):
        self.assertNotEqual(check_rating(22), "REMAJA", msg="Test Case is not Rating")

    # Negative Test Error is String
    def test_is_not_int(self):
        self.assertRaises(ValueError, check_rating, '2')


if __name__ == "__main__":
    unittest.main()