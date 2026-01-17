from decorator2 import my_decorator, uppercase_decorator

# Exemplo 1
@my_decorator
def my_function():
    print("hello, World!")
    
my_function()

# Exemplo 2
@uppercase_decorator
def text():
    return "hello, world"

print(text())