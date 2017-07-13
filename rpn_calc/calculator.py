"""Calculator module.
"""

import sys
from rpn_calc import OPERATIONS

class CalculatorRPN:
    """Reverse Polish Notation calculator class.
    """

    def __init__(self):
        self.__stack = []

    @property
    def stack(self):
        return self.__stack

    def add(self, value):
        operations = OPERATIONS
        if value not in operations.keys():
            self.stack.append(float(value))
        else:
            val2, val1 = self.stack.pop(), self.stack.pop()
            self.stack.append(operations[value](val1, val2))

    def __len__(self):
        return len(self.stack)

    def display(self):
        for i in self.stack:
            print(i)

def main():
    calculator = CalculatorRPN()
    for val in sys.argv[1:]:
        calculator.add(val)
    calculator.display()
