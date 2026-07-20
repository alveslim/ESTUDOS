class Pessoa:

    def __init__(self, altura, cpf) -> None:

        self.altura = altura

        self.__cpf = cpf

       

    def apresentar(self):

        print(f"Altura: {self.altura}")

        self.__coletar_cpf()

    # metodo que so pode ser acessado dentro da classe, ou seja, é privado

    def __coletar_cpf(self):

        print(f"CPF: {self.__cpf}")

       

jorge = Pessoa(1.75, "123.456.789-00")

#jorge.apresentar() # ira mostrar o cpf

#jorge.__coletar_cpf() # ira dar erro, pois o metodo é privado e so pode ser acessado dentro da class
#print(dir(jorge))

#print(jorge._Pessoa__cpf)
jorge._Pessoa__cpf = "999-653.324-99"
jorge.apresentar()
