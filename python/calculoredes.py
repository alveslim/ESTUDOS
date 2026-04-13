import ipaddress

# Este código calcula informações sobre uma rede IPv4 
# usando a biblioteca ipaddress do Python.

rede = ipaddress.IPv4Network('10.20.30.45/26', strict=False)

print(f"Rede: {rede.network_address}")
print(f"Máscara: {rede.netmask}")
print(f"Broadcast: {rede.broadcast_address}")
print(f"Primeiro Host: {rede[1]}")
print(f"Último Host: {rede[-2]}")
print(f"Total de Hosts utilizáveis: {rede.num_addresses - 2}") # - 2 para excluir o endereço de rede e o endereço de broadcast


