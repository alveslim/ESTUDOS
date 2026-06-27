# Web Scraping

# 1. Importando as ferramentas que vamos usar
import requests
from bs4 import BeautifulSoup

# 2. Definindo a URL do site que queremos raspar
url = "http://quotes.toscrape.com/"

# 3. Fazendo a requisição para o site (simulando um navegador acessando a página)
resposta = requests.get(url)

# Verificamos se o acesso deu certo (o código 200 significa "Sucesso!")
if resposta.status_code == 200:
    print("Conseguimos acessar a página!\n")
    
    # 4. Transformando o texto puro (HTML) em um objeto que o BeautifulSoup entende
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    
    # 5. Encontrando os dados
    # No HTML desse site, cada citação está dentro de uma <div> com a classe "quote"
    citacoes = sopa.find_all('div', class_='quote')
    
    # 6. Extraindo texto de cada citação encontrada
    for citacao in citacoes:
        # O texto da frase está num <span> com a classe "text"
        frase = citacao.find('span', class_='text').text
        
        # O autor está num <small> com a classe "author"
        autor = citacao.find('small', class_='author').text
        
        # Mostrando o resultado na tela
        print(f"Frase: {frase}")
        print(f"Autor: {autor}")
        print("-" * 40)
else:
    print(f"Erro ao acessar a página. Código: {resposta.status_code}")
    
"""
 RegrA (Ética e Realidade)

Embora seja uma ferramenta poderosa, nem todo site permite ser "raspado". Fazer requisições rápidas demais pode sobrecarregar o servidor do site (agindo como um ataque de negação de serviço, DDoS).

    Verifique o robots.txt: Sempre adicione /robots.txt ao final da URL de um site (ex: site.com/robots.txt) para ver quais páginas o dono do site permite ou proíbe que robôs acessem.

    Tenha bom senso: Se for raspar muitas páginas, coloque pausas no seu código (usando time.sleep(2)) para não derrubar o site de ninguém.

    Sites dinâmicos: O requests e BeautifulSoup só leem HTML estático. Se o site usar muito JavaScript para carregar dados (como redes sociais infinitas), você precisará de bibliotecas mais avançadas, como o Selenium ou Playwright.
"""