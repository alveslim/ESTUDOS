import tkinter as tk

#- criando a janela

window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de tarefas")

#- adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

#- adicionando o label
label = tk.Label(frame, text = "Hello, World")
label.pack(fill='x', expand=True)

#- adicionando input text
frase_lab =  tk.Label(frame, text = "Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# funcao para alterar o texto do label
def click():
    label.config(text = frase_inp.get())

#- adicionando botao
button = tk.Button(frame, text = "Enviar", command=click)
button.pack()


window.mainloop()