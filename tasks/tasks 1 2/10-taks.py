teams = {}
done = False

def print_teams():
    print("Teams:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} players)")
        
def print_team_players(team):
    print(f"Jogadores do {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

while not done:
    # 
    print("What you want to do?")
    print("1. Add a team")
    print("2. Remove a team")
    print("3. Show all teams")
    print("4. Add a player to a team")
    print("5. Remove a player from a team")
    print("6. Show all players in a team")
    print("7. Exit")
    
    choice = input(">>")
    if choice == "1":
        team_name = input("Enter team name: ")
        teams[team_name] = {"name": team_name, "players": []}
        print(f"Team '{team_name}' added.")
        pass
    elif choice == "2":
        print_teams()
        team_num = int(input("Enter team number to remove: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            #print(teams[team_name])
            del teams[team_name]
            print(f"Team '{team_name}' removed.")
        pass
    elif choice == "3":
        print_teams()
        pass
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            player_name = input("Informe o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time.")
        else:
            print("Número do time inválido")
        pass
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador para remover: "))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num-1]
                print("Jogador removido do time.")
            else:
                print("Número do jogador inválido.")
        else:
            print("Número do time inválido.")
        pass
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o número do time para listar jogadores: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
        else:
            print("Número do time inválido.")
        pass
    elif choice == "7":
        done = True
    else:
        print("Invalid choice. Please try again.")