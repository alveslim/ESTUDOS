class MinhaClasse:
    
    def __init__(self, info, elemento): # meotodo construtot é o primeiro!
        #print("estou no construtor da classe")
        self.atributo_1 = "valor do atributo 1"
        self.atributo_2 = [1, 2, "A"]
        self.atributo_3 = elemento
        self.atributo_4 = {"chave": "valor"}
        self.new_atribute = info
        print(self.new_atribute)
    
    def metodo_1(self):
        print("Minha acao 1")
        print(self.atributo_2)
        print(self.atributo_3)
        print(self.atributo_4)
        return "Retorno da acao 1"
    
    def metodo_2(self, num):
        self.__init__(self.new_atribute, self.atributo_3)
        print(self.atributo_2[1] + num)

# objeto       # Classe -> instanciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor", "elemento aqui")
# printando o retorno do metodo_1
#response = minha_classe.metodo_1()
reposta = minha_classe.metodo_2(20)
#print(response)
print(reposta)

 