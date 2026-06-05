a----------------------------------
# -- Git Repo Remotos --
----------------------------------
# git clone url-do-repositorio name-opcional
L> criar uma copia dele onde voce irá trabalhar

# git push nome-do-remote nome-da-branch
L> quando possuir commits que deseja integrar no
repositorio remoto, envie-os com esse comando

# git pull nome-do-remote nome-da-branch
L> quando quiser sicronizar o remoto para atualizar
o local

# git push origin master --force
L> empurra mole mesmo 

----------------------------------
# -- criando ssh --
----------------------------------
# ssh-keygen -C "seuEmail@.com"
L> criando chave ssh...
L> existe outras configuracoes
* por meio de https, github desktop e etc..

entrar no pw admin
L> eval "$(ssh-agent -s)"
L> Set Service -Name ssh-agent -StartupType Automatic
   Start-Service ssh-agent

cd na pasta que ira utilizar o ssh
# ssh-add ~/.ssh/id_ed25519
# ssh-add /home/flavio/.ssh/id_ed25519
L> na pasta do seu projeto pelo terminal, para utilizar a sua chave 
ssh

# cat id_ed25519;pub
L> lista conteudo do arquivo
L> tem q entrar no diretorio do arquivo (ls -la)--> para listar arq 
e adicionar no github

git remote set-url origin git@github.com:seu-usuario/seu-repositorio.git
git clone git@github.com:seu-usuario/seu-repositorio.git
ssh -T git@github.com