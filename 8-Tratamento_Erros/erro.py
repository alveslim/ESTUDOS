try:
    print(ola) # NameError
    num1 = 3
    num2 = 0
    response = num1 / num2
    print(response) # ZeroDivisionError
finally:
    num3 = 3
    num4 = "oi"
    responsee = num3 / num4
    print(responsee) # TypeError