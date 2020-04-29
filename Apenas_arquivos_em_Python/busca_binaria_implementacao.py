# -*- coding:utf-8 -*-

primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] 
# Os primeiros 25 números primos

min_indice = 0
max_indice = 24

if(primos[(max_indice+min_indice)/2] == 67):
    print("Você acertou!!!")
    print("O número 67 é o {} item" .format((max_indice+min_indice)/2))
elif (primos[(max_indice+min_indice)/2] < 67):
    print("A tentativa caiu no número {} que é menor que 67".format(primos[(max_indice+min_indice)/2]))
    min_indice = ((max_indice+min_indice)/2)+1
else:
    print("A tentativa caiu no número {} que é maior que 67".format(primos[(max_indice+min_indice)/2]))
    max_indice = ((max_indice+min_indice)/2)-1

print("O novo indice será: {}".format((max_indice+min_indice)/2))

if(primos[(max_indice+min_indice)/2] == 67):
    print("Você acertou!!!")
    print("O número 67 é o {} item" .format((max_indice+min_indice)/2))
elif (primos[(max_indice+min_indice)/2] < 67):
    print("A tentativa caiu no número {} que é menor que 67".format(primos[(max_indice+min_indice)/2]))
    min_indice = ((max_indice+min_indice)/2) + 1
else:
    print("A tentativa caiu no número {} que é maior que 67".format(primos[(max_indice+min_indice)/2]))
    max_indice = ((max_indice+min_indice)/2) - 1

