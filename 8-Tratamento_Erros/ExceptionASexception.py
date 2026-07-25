try:
    num1 = 3
    num2 = 0
    response = num1 / num2
    print(response)
except NameError:
    print("esse nome nao existe")
except ZeroDivisionError:
    print('0') # Pq qlqr numero dividido por 0 é iguaol a zero
except Exception as exception:
    print(exception) # $ DivisionByZero
    print(isinstance(exception, ZeroDivisionError)) # exception e uma instancia de ZeroDivsionError
finally:
    print("Venha para k independentemente")