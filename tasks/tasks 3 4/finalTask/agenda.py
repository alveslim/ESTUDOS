"""Desenvolva uma agenda de contatos persistindo as informações em arquivo.
O programa deve seguir as especificidades:

    Criar o arquivo Agenda contendo quatro métodos:
        Um método para adicionar contato.
        Um método para listar contatos.
        Um método para remover contatos.
    Criar um arquivo principal para a aplicação que importar o módulo de 
    agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção 
    escolhida."""

import os 

#modulo de persistencia de dados, para salvar os contatos em um arquivo de texto
# bugs marcados em <<<<, o arquivo txt esta sendo criado fora da pasta... so atualizar o caminho do arquivo para "tasks/tasks 3 4/finalTask/agenda.txt" ou usar o caminho relativo, como "agenda.txt" e colocar o arquivo txt na mesma pasta do codigo


def adicionar_contato(nome, telefone):
    with open("agenda.txt", "a") as file:
        file.write(f"{nome} - {telefone}\n")
        
def listar_contatos():
    if not os.path.exists("agenda.txt"):
        print("Nenhum contato encontrado.")
        return
    with open("agenda.txt", "r") as file:
        for line in file:
            print(line.strip()) # podemos mudar para uma janela <<<<
        
def remover_contato(nome):    
    with open("agenda.txt", "r") as file:
        lines = file.readlines()
    with open("agenda.txt", "w") as file:
        for line in lines:
            if not line.startswith(nome):
                #por um erro se nao houver contato <<<<
                file.write(line) # bug esta aparecendo o contato removido 4 vzs... <<<<
                print(f"Removendo contato: {nome}")
                      
#adicionar_contato("João", "123456789")
#listar_contatos()
#remover_contato("pedro")