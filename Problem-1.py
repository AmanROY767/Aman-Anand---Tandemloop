# Problem-1: Calculator using Class

class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"



a = input("Enter first number: ")
b = input("Enter second number: ")
operation = input("Enter operation (add, subtract, multiply, divide): ")

calc = Calculator(a, b)
print("Result:", calc.operate(operation))
