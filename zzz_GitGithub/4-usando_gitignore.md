/////////////////////////////////////////////////////////////////////

.vscode | node_modules | .env | bin 
exemplo de coisas que gostaria de manter fora do repositorio
L> solucao?

# O .gitignore
# uploads/images
L>se digitar por exemplo .vscode dentro do arquivo, ele vai parar de 
ser monitorado pelo git.

# uploads/ *
L> ignora toda a pasta
# !uploads/.gitkeep
L> nao ignora tal arquivo ou pasta

# .gitkeep 
L> manter uma pasta para monitora-la