# test_calculator.py
import unittest
from message.utils import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This method is called before each test method
        self.calc = Calculator()

    def test_add(self):
        # Test addition of positive numbers
        self.assertEqual(self.calc.add(1, 2), 3)
        # Test addition of a negative and positive number
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test addition of two negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_divide(self):
        # Test division of positive numbers
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test division by zero, expecting a ValueError
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
