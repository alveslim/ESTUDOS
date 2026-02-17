1 - APRENDIZADO COMANDOS GIT 

git init --help & git --help 
cd pasta/           #procura diretorio
cd .ssh2            #ACESSANDO
mkdir criando_pasta # criando uma pasta
cd criando_pasta 
code .              # abre a pasta atual acessada por vscode
ls -la              #listando
-------------------------------------------------

git init            # inicializa um novo repositório

U -- Nao Registrado 
A -- Alteracao para Preparacao
M -- Modificado
-------------------------------------------------
git status          # exibe a situacao autal da working
                    # tree (Oq foi modificado e oq esta
                    preparado.)
git add arq.py      # registra para Preparacao
git add .           # adiciona todos 
git rm --cached arq # remove do cache de Preparacao (Nao monitorado)
--------------------------------------------------
Comprometimento

git commit -m "comentario de alteracao"
git log             # mostra historico 
git diff            # config pendentes, mostra a diferenca
                      entre o arquivo anterior e atual.
git restore         # reverter
