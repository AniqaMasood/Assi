# from src.square_root import square_root

# def test_sq_rt():
#     assert square_root(2,4) == 1.4142

import unittest
from src.square_root import square_root

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual(square_root(2,4) , 1.4142)

if __name__ == '__main__':
    unittest.main()