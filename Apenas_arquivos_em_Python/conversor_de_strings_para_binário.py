# -*- coding: utf-8 -*-

print ("=== Este programa é um conversor de palavras para uma base específica ===")
palavra = input("Digite sua palavra para que ela seja convertida (tudo em minúsculo): ");

quantidade = len(palavra)

conta_caractere = 0

for caractere in palavra:
    conta_caractere +=1
    if(caractere == "a"):
        print("01100001")
    elif(caractere == "b"):
        print ("01100010")
    elif(caractere == "c"):
        print ("01100011")
    elif(caractere == "d"):
        print ("01100100")
    elif(caractere == "e"):
        print("01100101")
    elif(caractere == "f"):
        print("01100110")
    elif(caractere == "g"):
        print("01100111")
    elif(caractere == "h"):
        print("01101000")
    elif(caractere == "i"):
        print("01101001")
    elif(caractere == "j"):
        print("01101010")
    elif(caractere == "k"):
        print("01101011")
    elif(caractere == "l"):
        print("01101100")
    elif(caractere == "m"):
        print("01101101")
    elif(caractere == "n"):
        print("01101110")
    elif(caractere == "o"):
        print("01101111")
    elif(caractere == "p"):
        print("01110000")
    elif(caractere == "q"):
        print("01110001")
    elif(caractere == "r"):
        print("01110010")
    elif(caractere == "s"):
        print("01110011")
    elif(caractere == "t"):
        print("01110100")
    elif(caractere == "u"):
        print("01110101")
    elif(caractere == "v"):
        print("01110110")
    elif(caractere == "w"):
        print("01110111")
    elif(caractere == "x"):
        print("01111000")
    elif(caractere == "y"):
        print("01111001")
    elif(caractere == "z"):
        print("01111010")
    elif(caractere == " "):
        print("00100000")
        
print ("Obrigado por utilizar o meu programa")