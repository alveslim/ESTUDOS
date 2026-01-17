###Use no terminal:
""""
                python -m venv .venv 
                cd .\.venv\
                cd .\Scripts\
                Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
                .\activate
                """
                
##Voltando os diretorios
"cd .." 
                
###Criando o diretorio de requerimentos:       
"""
                pip freeze p
                 pip freeze -1 > requirements.txt
                pip install -r .\requirements.txt 
                deactivate ##desativa o venv
                """
                
### Gerando instalador app
###pyinstaller --onefile .\12-tkinter.py