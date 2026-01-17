gameName = input("Enter game name: \n")
qtdRating = 0
totalRating = 0
rating = 0
avarage = 0 

while (rating != -1):
    rating = int(input("Enter game rating (1-10): \n"))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        avarage = totalRating / qtdRating
print(f"the avarege rating for the game {gameName} if {avarage:.2f}")


