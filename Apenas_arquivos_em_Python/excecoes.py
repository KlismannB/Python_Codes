# -*- coding: utf-8 -*-

lista0 = [1,2,3,4]

try:
    for item in range(len(lista0)+1):
        print (lista0[item])
except:
    print("Foi encontrado um limite no numero de itens, seu contador parou em: {}" .format(item))
    
try:
    print (lista0[3])
except:
    print ("Não existe esse item")
else:
    print ("O item existe")
finally:
    print ("Prosseguindo normalmente o programa")
    
lista = [1,2,3,4]

try:
    valor = int(input("Digite 1 ou 2: "))
    if (valor == 1):
        print (lista[4])
    elif (valor == 2):
        1/0
    else:
        print ("Apenas 1 ou 2")
        exit()
except(IndexError,ZeroDivisionError):
    print ("Detectada exceção do tipo IndexError ou ZeroDivisionError")

try:
    print (lista[4])
except Exception as e:
    print (e)
    
try:
    print (lista[4])
except: # except Exception:
    print ("Passei")
    pass

try:
    raise ZeroDivisionError
except:
    print ("RAISE forcou exceção do tipo ZeroDivisionError, sendo capturado pelo EXCEPT")
    
print ("O texto será mostrado na tela")

numero = int(input("Digite um número: "))

texto = input("Digite um texto: ")

print (type(numero))
print (type(texto))