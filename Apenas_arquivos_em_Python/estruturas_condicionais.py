# -*- coding: utf-8 -*-

# As estruturas condicionais funcionam muito para as lógicas de programação
# Funciona com um if (se) e um else (se não)

x = 10
y = 4

if(x >= y): # Confere se a condição é verdadeira
    print ("Banana") # Caso sim, este comando é executado
else:
    print ("Maçã") # Caso não, este comando é executado

x = 4
y = 10
    
if(x >= y):
    print ("Banana") # Caso sim, este comando é executado
else:
    print ("Maçã") # Caso sim, este comando é executado

# Temos também o elif (else if (se não, se...))

x = 10
y = 4
z = 10

if (x <= y):
    print ("Banana") # Caso sim, este comando é executado
elif(x != y and x == z):
    print ("Uva") # Caso sim, este comando é executado
else:
    print ("Maçã") # Caso nenhum, este comando é executado