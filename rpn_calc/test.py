import unittest

from .calculator import CalculatorRPN


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorRPN()

    def test_stack_size(self):
        self.calculator.add(10)
        self.assertEqual(len(self.calculator), 1, 'incorrect stack size')
        self.calculator.add(20)
        self.assertEqual(len(self.calculator), 2, 'incorrect stack size')

    def test_stack_value(self):
        self.calculator.add(1)
        self.assertEqual(self.calculator.stack, [1], 'incorrect stack value')

    def test_stack_operation_add(self):
        self.calculator.add('2')
        self.calculator.add('5')
        self.calculator.add('+')
        self.assertEqual(self.calculator.stack, [7], 'incorrect stack operation value')
