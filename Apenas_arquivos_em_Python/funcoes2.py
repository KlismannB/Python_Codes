# -*- coding: utf-8 -*-

def imprime():
    print ("Funcao IMPRIME")
def imprime_nome(nome):
    print ("O seu nome é: ", nome)
def soma(a, b):
    print ("A + B = ", a+b)
    
imprime()
nome = input("Digite o seu nome: ")
imprime_nome(nome)
a,b = int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: "))
soma(a,b)

def altera_num():
    num = 10
    
num = 2
altera_num()

print ("Valor de num: ", num)