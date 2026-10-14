import numpy as np

class Calculator:
     def __init__(self, x, y, operator):
            self.x = x
            self.y = y
            self.operator = operator

     def solution(self):

        if self.operator == '+':
            return np.add(self.x, self.y)
        elif self.operator == '-':
            return np.subtract(self.x, self.y)
        elif self.operator == '*':
            return np.multiply(self.x, self.y)
        elif self.operator == '/':
            if self.y != 0:
                return np.divide(self.x, self.y)
            else:
                return "Error! Division by zero."
        else:
            return "Invalid operator."

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")


p1 = Calculator(x, y, operator)
result = p1.solution()
print(f"The result of {p1.x} {p1.operator} {p1.y} is: {result}")