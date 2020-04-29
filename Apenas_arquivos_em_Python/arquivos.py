# -*- coding: utf-8 -*-

texto = "Olá mundo!"

# ARQUIVOS EM TXT

with open("Arquivo_novo.txt", "r") as arquivo:
    print (arquivo.read())
    
with open("Arquivo_novo.txt", "w") as arquivo:
    arquivo.write(texto)
    
with open("Arquivo_novo.txt", "a") as arquivo:
    arquivo.write(texto)
    
# ARQUIVOS EM BINÁRIO

with open("Arquivo_novo.txt", "rb") as arquivo:
    print (arquivo.read())
with open("Arquivo_novo.txt", "wb") as arquivo:
    print (arquivo.read())
    
