# Question:
# Create a simple calculator that accepts two numbers and an operation.
# Support +, -, *, and / operations.
# Handle division by zero and invalid operations.

def main():
    print("Simple Calculator")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculator(a, b, operation)
    print(f"Result: {result}")


def calculator(a, b, operation):
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b

    else:
        return "Error: Invalid operation"

main()