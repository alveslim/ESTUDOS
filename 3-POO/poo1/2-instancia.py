class Movie:
    name = ""
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0
    
# - primeiro filme 
movie = Movie()
movie.name =  "Super Mario Bros"
movie.yearLaunch = 2023
movie.includePlan = False
movie.note =  5.0
movie.durationMinutes = 130

# - segundo filme 
movie2 = Movie()
movie2.name =  "Avatar 2"
movie2.yearLaunch = 2024
movie2.includePlan = True
movie2.note =  4.8
movie2.durationMinutes = 220

print("--Dados do Filme--")
print(f"Nome do filme: {movie.name} \nAno de lancamento: {movie.yearLaunch}")
print(f"Nome do filme: {movie2.name} \nAno de lancamento: {movie2.yearLaunch}")