def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

a = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
b = int(input("Enter second number: "))

if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = subtract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = divide(a, b)
else:
    result = "Invalid operation"

print("Result is:", result)
