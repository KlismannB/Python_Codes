# -*- coding: utf-8 -*-

# Mais alguns operadores, agora operadores lógicos
# Que são os operadores: and, or e not

'''
Tabela verdade do operador 'and'

    True and True = True
    True and False = False
    False and True = False
    False and False = False
    
'''
print("Saídas do operador lógico and:")

x = True
y = True

print (x and y)

x = True
y = False 

print (x and y)

x = False
y = True

print (x and y)

x = False
y = False

print (x and y)

'''
Tabela verdade do operador 'or'

    True or True = True
    True or False = True
    False or True =  True
    False or False = False
    
'''
print("Saídas do operador lógico or:")

x = True
y = True

print (x or y)

x = True
y = False

print (x or y)

x = False
y = True

print (x or y)

x = False
y = False

print (x or y)

'''
O operador lógico not funciona como um inversor do valor
original da afirmação

    not True = False
    not False = True
    
'''
print("Saídas do operador lógico not:")

x = False
y = True

print (not x)
print (not y)
