import webbrowser

done = False
while not done:
    print("O que voce deseja fazer?")
    print("1 - Abrir Google")
    print("2 - Abrir YouTube")
    print("3 - Sair")
    
    choice = input(">")
    
    if choice == "1":
        webbrowser.open("http://www.google.com")
    elif choice == "2":
        webbrowser.open("http://www.youtube.com")
    elif choice == "3":
        done = True
    else: 
        print("Escolha invalida, tente novamente.")
    