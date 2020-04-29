# -*- coding: utf-8 -*-

dicionario = {
    "chave0" : "valor1",
    "chave1" : "valor2",
    3 : ["zero", "um", "dois"]
}

print ("O valor da chave0 é: ", dicionario["chave0"])

print ("O valor da chave1 é: ", dicionario["chave1"])

print ("O valor 3 armazena a seguinte lista", dicionario[3])

print ("Alterando o valor do item 0 de 3!")

dicionario[3][0] = "menos um"

print (dicionario[3])
