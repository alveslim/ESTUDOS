#Criacao de Metodo de Classe (Instancia)

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        print("--Dados do Filme--")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está no Plano? {self.includedPlan}")
        print(f"Avaliação: {self.note}")
        print(f"Duração: {self.durationMinutes}")
        print("\n")
        
mario = Movie("Super Mario Bros", 2023, False, 5.0, 125)
top_gun =Movie("Top Gun Maverick", 2022, True, 4.5, 160)
mario.technical_sheet()
top_gun.technical_sheet() 

        