array = [1, 1, 1, 2, 3, 4, 5, 2, 2, 3, 5, 5, 5, 5, 5 ,4, 6]
complete = False
quantidade = 1 
valor = 1
indice = 1

for i in range(0, len(array) - 1):
    for j in range(i + 1, len(array) - 2):
        if(array[i] == array[j]):
            valor += 1
            
            if(quantidade < valor):
                quantidade = valor
                indice = i
    valor = 1
                                
print("{} eh o item que mais aparece e aparece {} vezes".format(array[indice], quantidade)) 