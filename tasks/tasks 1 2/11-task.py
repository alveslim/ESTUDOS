import subprocess

command = ["ping", "-n", "4", "8.8.8.8"]
result = subprocess.run(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                        )

for line in result.stdout.splitlines():
    line = line.strip()
    # print(line.find('tempo=')) vai dar a posicao, dito isso -1 nao e valido
    
    posicao = line.find('tempo=')
    if posicao != -1:
        
        clean_line = line[posicao:]
        tempo_isolado = clean_line.split(" ")[0]
        just_valuer = tempo_isolado.replace("tempo=", "")
        
        print(f"Tempo resposta: {just_valuer.upper()}")