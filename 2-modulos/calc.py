#modulos/calc.py
# Calculator module with basic arithmetic functions

def sum (a, b):
    result = a + b
    return result

def subtract (a, b):
    result = a - b
    return result

def multiply (a, b):
    result = a * b
    return result

def divide (a, b):
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    return result