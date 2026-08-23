import subprocess

try:
    # Tenta pingar um IP inválido com tempo limite de 3 segundos
    resultado = subprocess.run(
        ["ping", "-n", "4", "google.com"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=5  # Se passar de 3s, o Python interrompe
    )
    print(resultado.stdout.decode("utf-8", errors="replace"))
    #print(f"pacote: {resultado}")
    
    for linha in resultado.stdout.splitlines():
        print(f"> {linha.strip()}")
except subprocess.TimeoutExpired:
    print("O comando demorou muito e foi cancelado pelo Python.")