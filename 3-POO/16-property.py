class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self): # Getter pega o valor
        return self._name 
    
    @name.setter 
    def name(self, value): # Setter valida e seta o valor
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

"""pessoa = person(132321, 30) # This will raise a TypeError
print(vars(pessoa))"""

pessoa2 = person("Alice", 25) # This will work fine
print(vars(pessoa2))

