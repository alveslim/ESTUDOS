#Metodo especial 

class Movie: #mesma coisa na instancia, so facilitando e tendo dois metodos 
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self): # fzd referencia direto a classe 
        return f"Filme: {self.name}"

movie = Movie("Super Mario Bros", 2023, False, 5.0, 130)
movie2 = Movie("Avatar 2", 2023, False, 4.5, 220)
print(movie.name)
print(movie2.name)
print(movie)
print(movie2)
