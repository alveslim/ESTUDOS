# mapear a rede local. O script calcula todos os hosts da sua 
# sub-rede atual (ex: /24) e tenta dar um ping em cada um.

"""
# Mostre quais IPs estão ativos e quais estão livres. Isso é 
# ótimo para entender a diferença entre o Endereço de Rede 
# (que não responde) e os Hosts.Mostre quais IPs estão ativos 
# e quais estão livres. Isso é ótimo para entender a diferença 
# entre o Endereço de Rede (que não responde) e os Hosts.
"""
#Use a biblioteca subprocess para disparar o comando de ping do sistema operacional.

import socket 
import requests 

ip = requests.get('https://ifconfig.me/ip').text.strip()
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)

print(f"Meu IP: {ip}")
print(f"Meu IP local: {ip_local}")
