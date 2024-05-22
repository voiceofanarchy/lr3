import unittest
from math_functions import add, subtract

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(2.5, 3.1), 5.6)
        self.assertEqual(add('a', 3), "Invalid input")
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5.5, 3.1), 2.4)
        self.assertEqual(subtract('a', 3), "Invalid input")

if __name__ == '__main__':
    unittest.main()
