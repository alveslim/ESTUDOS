import subprocess

try:
    # Tenta pingar um IP inválido com tempo limite de 3 segundos
    google = subprocess.run(
        ["ping", "-n", "4", "google.com"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=5  # Se passar de 3s, o Python interrompe
    )
    print(google.stdout.decode("utf-8", errors="replace"))
    #print(f"pacote: {google}")
    
    for linha in google.stdout.splitlines():
        print(f"> {linha.strip()}")
except subprocess.TimeoutExpired:
    print("O comando demorou muito e foi cancelado pelo Python.")
    
    
# 1. Executa o comando e captura a saída
resultado = subprocess.run(["python", "--version"], capture_output=True, text=True)
texto_bruto = resultado.stdout  # Ex: "Python 3.11.4\n"

# 2. Aplicando métodos de string:
texto_limpo = texto_bruto.strip()                 # Remove o \n do final -> "Python 3.11.4"
palavras = texto_limpo.split(" ")                 # Divide por espaço -> ['Python', '3.11.4']
versao = palavras[1]                              # Fatiamento/Indexação -> "3.11.4"
maiusculo = texto_limpo.upper()                   # Caixa alta -> "PYTHON 3.11.4"
invertido = texto_limpo[::-1]                     # Invertendo a string

print(f"Versão extraída: {versao}")
print(f"Texto em maiúsculo: {maiusculo}")
print(f"Texto invertido: {invertido}")