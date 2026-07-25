class MinhaClasse:
    
    static = "flavio" # uma copia para todos
    
    def __init__(self, estado) -> None:
        self.estado = estado
        
    def print_variavel_classe(self):
        print(self.static)
    
    @classmethod    
    def alteracao_variavel_classe(cls): # --> cls acessando o contexto geral
        cls.static = "alteracao"

# Instanciou        
obj = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj.print_variavel_classe()  # $ flavio
obj.alteracao_variavel_classe() # --> alterando todos os objetos

print(obj.static) # $ alteracao
print(obj2.static) # $ alteracao
print(MinhaClasse.static) # $ alteracao
