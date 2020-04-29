# -*- coding: utf-8 -*-
import socket

dominio = "dominio.com"

nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

for nome in nomes:
    DNS =  nome + "." + dominio # Concatena cada nome da lista de nomes com o nomde de domínio, gerando o nome DNS
    try:
        print(DNS + ": " + socket.gethostbyname(DNS)) # usa o método gethostbyname() da biblioteca socket para determinar o endereço IP a partir de um nome DNS, se esse metodo nao conseguir resolver o nome DNS para um endereco IP, sera gerada uma excessao do tipo gaierror, portando nao eh um nome de dominio valido. Caso o host utilize mais de um IP para responder por apenas um único nome, utilize o método gethostbyname_ex() 
    except socket.gaierror():
        pass
