num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))
operation = input("Enter operation (+, -, *, /): \n")

if operation == "+": 
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else: 
    print("Operation is not addition.")
    result = None
print(f"The result is: {result:.2f}")

