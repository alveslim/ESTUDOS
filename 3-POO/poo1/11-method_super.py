class Phone:
    def __init__(self, brand, model, price):
        self._brand =  brand
        self._model = model
        self._price = price
        
    def __str__(self):
        return f"{self._brand}{self._model}"
    
    @staticmethod
    def make_a_call(phone_num):
        return f"Calling {phone_num}..."

class Smartphone(Phone):
    def __init__(self, brand, model, price, ram, internal_memory, back_camera):
        super().__init__(brand, model, price) # Uso do super()
        # Continuando a inicialização da subclasse
        

        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        
Moto =  Phone('Moto','G7',1000)
print(Moto)
Moto.make_a_call(232132)
print(f"Valor do {Moto._brand}{Moto._model} é {Moto._price()}")
print(vars(Moto))

Iphone = Smartphone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(32142342)
print(f"Valor do {Iphone._brand}{Iphone._model} é {Iphone._price()}")
print((Iphone))