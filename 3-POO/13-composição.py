class animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
class fish(animal):
    race = ""
    
class parrots(animal):
    color = ""
    
class zoo: #Composicao, quais animais estao no zoo
    def __init__(self):
        self.animals_dict = {} # cria nosso dicionario vazio, poderemos add
                               # nossos animais aqui 
            
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category  # Adiciona o animal no dicionario
        # animal.name sera a chave e animal.category sera o valor
        # Ex: {"Nemo": "Fish"}
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values(): # Percorre os valores do dicionario
            if animal == category: # Compara se o valor é igual a categoria passada como parametro.
                                   # Como? Ex: "Fish" == "Fish"
                result += 1
                # Conta quantos animais daquela categoria existem
        return f"Total of {result} in the zoo is {category} "
meuZoo = zoo()
fish1 = fish("Nemo", "Fish") #name, category
fish2 = fish("Dory", "Fish") #

print(vars(fish1))
print(vars(fish2))
meuZoo.add_animal(fish1) # Vai adicionar o nemo no zoo. +1
meuZoo.add_animal(fish2) # Vai adicionar o dory no zoo. +2
print(meuZoo.total_of_category("Fish"))
