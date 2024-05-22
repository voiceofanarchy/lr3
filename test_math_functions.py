import unittest
from math_functions import add, subtract

class TestMathFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5.0)
        self.assertEqual(add(-1, 1), 0.0)
        self.assertEqual(add(-1, -1), -2.0)
        self.assertEqual(add(2.5, 3.1), 5.6)
        self.assertEqual(add('2', '3'), 5.0)
        self.assertEqual(add('a', '3'), "Invalid input: First input is not a number")
        self.assertEqual(add('2', 'b'), "Invalid input: Second input is not a number")
        self.assertEqual(add('a', 'b'), "Invalid input: Both inputs are not numbers")
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2.0)
        self.assertEqual(subtract(-1, 1), -2.0)
        self.assertEqual(subtract(-1, -1), 0.0)
        self.assertEqual(subtract(5.5, 3.1), 2.4)
        self.assertEqual(subtract('5', '3'), 2.0)
        self.assertEqual(subtract('a', '3'), "Invalid input: First input is not a number")
        self.assertEqual(subtract('5', 'b'), "Invalid input: Second input is not a number")
        self.assertEqual(subtract('a', 'b'), "Invalid input: Both inputs are not numbers")

if __name__ == '__main__':
    unittest.main()
