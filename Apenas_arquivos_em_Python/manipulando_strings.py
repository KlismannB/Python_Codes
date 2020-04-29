# -*- coding: utf-8 -*-

nome = "Klismann"
sobrenome = "Barros"

# A funcao de concatenar é juntar duas strings
concatenacao = nome + sobrenome
print (concatenacao)

# Separando só com um espaço a mais, só por estética
concatenacao = nome + " " + sobrenome
print (concatenacao)

# Dá pra ver qual o tamanho da sua string usando a funcao 'len'
tamanho = len(concatenacao)
print (tamanho)

# Entenda as strings como uma lista de caracteres, então podemos acessar cada caractere pelo índice dele
print (nome[0])

# Você também pode selecionar até onde da string quer mostrar
print (nome[0:6])
