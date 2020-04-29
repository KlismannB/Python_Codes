# -*- coding: utf-8 -*-

# Estruturas de repetição possuem diversas aplicabilidades
# Uma delas, por exemplo é o 'while' que marca sua presença até em jogos
# em python

print ("Para x = 2")
x = 2

while x <= 4:
    print (x)
    x = x + 1
    
print ("Para x = 0")
x = 0

while x <= 10:
    print(x)
    x = x + 1

# Outra estrutura de repeticao é o 'for'

lista_de_inteiros  = [1, 2, 3, 4, 5]
lista_de_strings = ["Matrix", "Nemo", "Xuxa"]
lista_variada = [1.02, "Klismann", 13, True]

print ("Lista de strings:")
for filme in lista_de_strings:
    print (filme)
    
# Por fim a estrutura 'for range'

print ("for-range de um parametro")
# Mostrará de 0 até 10
for i in range(11):
    print (i)

print ("for-range de dois parametros")
# Mostrará de 10 até 20
for i in range(10,21):
    print (i)

print ("for-range de três parametros")
# Mostrará de 10 até 40 de dois em dois
for i in range(10,41,2):
    print (i)
