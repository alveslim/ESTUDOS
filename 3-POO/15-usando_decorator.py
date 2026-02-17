from decorator2 import my_decorator, uppercase_decorator, split_string

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

# Exemplo 3
@split_string
@uppercase_decorator
def example():
    return "Hello World from Python Decorators"
print(example())