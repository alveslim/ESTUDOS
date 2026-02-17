def funtion(fname, lname):
    print("First Name: " + fname)
    print("Last Name: " + lname)
funtion("John", "Doe")

def address(city, country="USA"):
    print(f"I live in {city}, {country}")

address("New York")
address("Los Angeles", "Canada")
address("Toronto", "Canada")

#Rating function]
def rate_game(qtdRating):
    sum = 0
    for i in range(qtdRating):
        note = float(input(f"Type the rating for game {i + 1} (1-10):\n"))
        sum += note
    print(f"The average rating is: {sum / qtdRating}")
    
rate_game(2)
