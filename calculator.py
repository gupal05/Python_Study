from calculator_operations import MathOperations

class Calculator:
    def __init__(self):
        self.math_operations = MathOperations()

    def perform_operations(self, a, b):
        print(f"{a} + {b} = {self.math_operations.add(a, b)}")
        print(f"{a} - {b} = {self.math_operations.subtract(a, b)}")
        print(f"{a} X {b} = {self.math_operations.multiply(a, b)}")
        print(f"{a} / {b} = {self.math_operations.divide(a, b)}")

# 실행 예제
if __name__ == "__main__":
    calculator = Calculator()
    calculator.perform_operations(10, 5)