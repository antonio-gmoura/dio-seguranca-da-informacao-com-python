import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco)

ip_network = "192.168.0.0/24"

rede = ipaddress.ip_network(ip_network, strict=False)

print(rede)

for ip in rede:
    print(ip)