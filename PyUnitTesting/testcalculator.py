# PyUnit Testing Activity
# Katrina Wilson
# ITSC 3155

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)
        self.assertEqual(Calculator.subtract(-2, 2), -4)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2), 6)
        self.assertEqual(Calculator.multiply(-2, 0), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(4, 2), 2)
        self.assertEqual(Calculator.divide(-2, 2), -1)


if __name__ == '__main__':
    unittest.main()