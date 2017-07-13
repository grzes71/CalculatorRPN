"""CalculatorRPN package.
"""

import operator


OPERATIONS = {
    '+':operator.add,
    '-':operator.sub,
    '/':operator.truediv,
    '*':operator.mul
}