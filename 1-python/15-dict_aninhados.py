import pprint
gamesDict = {
    "Call of Duty": {
        "genre": "FPS",
        "platforms": ["PC", "Xbox", "PlayStation"],
        "release_year": 2003
    },
    "Counter-Strike": {
        "genre": "FPS",
        "platforms": ["PC"],
        "release_year": 2000
    },
    "The Witcher 3": {
        "genre": "RPG",
        "platforms": ["PC", "Xbox", "PlayStation", "Nintendo Switch"],
        "release_year": 2015 
        }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#Buscar informações específicas
print("As plataformas de Call of Duty são:", gamesDict["Call of Duty"]["platforms"])  # Plataformas de Call of Duty

gamesDict["The Witcher 3"]["developer"] = "CD Projekt Red"  # Adicionando nova chave/valor
del gamesDict["Counter-Strike"]



