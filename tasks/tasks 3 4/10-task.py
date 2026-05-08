#Avaliação e Média da Nota de Filmes

#Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe 
#Filmes. Segue o escopo das funcionalidades:

#    Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de 
#    um filme passando uma nota com parâmetro e que essa nota seja salva no atributo 
#    específico da classe.
    
#    Assim que uma avaliação for realizada, deve ser incrementado o total de 
#    avaliadores daquele filme. Obs: Considere criar um atributo específico 
#    para esse fim.
    
#    Para cada filme ter uma nota de avaliação média que consiste na divisão 
#    do total de avaliação pelo total de avaliadores
import os
import time
import re

def check_character(int): # Verifica se a string contém caracteres não numéricos -- ainda nao incrementado
    rule = re.compile(f'[^0-9]')
    int = rule.search(int)
    return not bool(int)

def limpar_tela():
    # 'nt' significa Windows (New Technology)
    if os.name == 'nt':
        os.system('cls')
    else:
    # Para Mac e Linux (posix)
        os.system('clear')

class Movies: 
    name = ""
    reviews = 0 # total de avaliadores
    score = 0 # nota total do filme
    durationMinutes = 0
    

    def review(self, note):
        self.score += note # total de nota do filme score = score + note
        self.reviews += 1 # total de avaliadores reviews = reviews + 1
def menu():
    limpar_tela()
    print("=== AVALIAÇÃO DE FILMES ===")        
    name = input("Type the name of the movie: ")
    movie = Movies()
    movie.name = name
    while True: 
        note = float(input("Type the score of the movie: "))
        #if not check_character(note):
        #   print("Invalid input. Please enter a valid number for reviews.")
        #    continue
        movie.review(note)
        continue_choice = input("Do you want to continnue? (y/n) ")
        if continue_choice == "n":
            input(f"The total score of the movie {movie.name} is {movie.score} and the total reviews is {movie.reviews}\n Press ENTER to exit...")
            time.sleep(2)
            limpar_tela()
            break
        elif continue_choice == "y":
            limpar_tela()
            print(f"=== AVALIAÇÃO DE FILMES ===\nMovie: {movie.name}\nTotal Score: {movie.score}\nTotal Reviews: {movie.reviews}")
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
            limpar_tela()
            continue
        
menu()