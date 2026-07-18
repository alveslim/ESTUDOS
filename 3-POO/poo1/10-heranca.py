class Animal:
    name = ""
    size = ""
    color = ""
    
    def eat(self):
        print(f"{self.name} está comendo.")
        
class Horse(Animal):
    race =  ""
    
    def run(self):
        print(f"{self.name} está correndo.")
        
class Lion(Animal):
    mane =  True
    
    def hunt(self):
        print(f"{self.name} está caçando.")

h = Horse()
h.name = "Carpeado"
h.size = "Grande"
h.color = "Marrom"
h.run()
h.eat()

l = Lion()
l.name = "Simba"
l.size = "Médio"
l.hunt()