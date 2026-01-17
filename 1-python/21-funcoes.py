def wellcome():
    print("Welcome to the Game Rating System!")
    
#function for calculating
def sum():
    return 2 + 2

#register game

def create_game():
    name = input("Type the game name:\n")
    yearLaunch = int(input("Type the year of launch:\n"))
    gamePrice = float(input("Type the game price:\n"))
    planeInclueded = bool(input("Is the plane included? (True/False):\n"))
    noteRating = float(input("Type the game rating (1-10):\n"))
    
    print(f"{name} - R$ {gamePrice}" )
    
create_game()