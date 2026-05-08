import google.generativeai as genai
import customtkinter as ctk

genai.configure(api_key="SUA_CHAVE_GEMINI_AQUI")

model = genai.GenerativeModel('gemini-1.5-flash')

def askquestion(text):
    response = model.generate_content(text)
    return response.text

print(askquestion("Qual é a capital da França?"))

#Nosferatu_Nokinglife

##########################################################################

#window = ctk.CTk()
#window.geometry("300x150")
#window.title("Gerenciador de tarefas")

#frame = ctk.CTkFrame(window)
#frame.pack(padx=10, pady=10, fill='x', expand=True)

#label = ctk.CTkLabel(frame, text= "CLAUDE IA API")
#label.pack(fill='x', expand=True)

#frase_lab = ctk.CTkLabel(frame, text="try to ask: ")
#frase_lab.pack(fill='x', expand=True)

#frase_inp = ctk.CTkEntry(frame)
#frase_inp.pack(fill='x', expand=True)
#mensagem = frase_inp.get()

#def click():
#label.config(text = frase_inp.get())

#button = ctk.CTkButton(frame, text="send", command=click)
#button.pack()

#label_chat = ctk.CTkLabel(frame, text= "Resposta da IA")
#label_chat.pack(fill='x', expand=True)

#window.mainloop()


