"""class MinhaClasse:
    def __init__(self, estado) -> None:
        self.estado = estado
        print(self.estado)
        
obj = MinhaClasse(True)
print(obj.estado)"""

class MinhaClasse:
    
    static = "flavio" # uma copia para todos
    
    def __init__(self, estado) -> None:
        self.estado = estado

# Instanciou        
obj = MinhaClasse(True)
obj2 = MinhaClasse(True)

# criando espelho
MinhaClasse.static = "programdor" # altera todas
obj.static = "olaMundo" # criou um espelho no objeto 
MinhaClasse.static = "pythonAqui" # muda so MinhaClasse>obj2 

print(obj.static)
print(obj2.static)
print(MinhaClasse.static)