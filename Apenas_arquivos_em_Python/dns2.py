import socket

dominio = "dominio.com"
with open("brute-force.txt") as arquivo:
    nomes = arquivo.read()
    
for nome in nomes:
    DNS = nome.strip("\n") + "." + dominio
    
    try:
        print (DNS + ": " + socket.gethostbyname(DNS))