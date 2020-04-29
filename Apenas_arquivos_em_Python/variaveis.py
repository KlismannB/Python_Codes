# -*- coding: utf-8 -*-

minha_variavel = "Olá mundo!" # Armazena na variavel 'minha_variavel'o texto (string) "Olá mundo!"

Minha_variavel = "Olá mundo!" # Esta variável, apesar de ter "o mesmo nome" e o mesmo conteúdo da outra variável
                              # não é a mesma coisa, pois python possui sensibilidade a maiúsculas e minúsculas
                              # em inglês, isso se chama ser Case Sensitive
                              
print ("A variável string:")
# Exibindo o conteúdo das variaveis 'minha_variavel' e 'Minha_variável'
print (minha_variavel)
print (Minha_variavel)


numero_inteiro = 10 # Atribui a variavel 'numero_inteiro' o numero 10

print("A variável inteira:")
# Exibindo o conteúdo da variável 'numero_inteiro'
print (numero_inteiro)

numero_decimal = 3.141592653589793 # Atribui algumas casas decimais do número pi à variável numero_decimal
                                   # Numeros decimais podem ser chamados de pontos flutuantes (float)
 
print ("A variável decimal:")                                  
print (numero_decimal) # Exibe o conteúdo da variável 'numero_decimal'

booleano_verdadeiro = True # Essa variável booleana é uma espécie de baixo nível em python
                           # tem como sentido único dar veradeiro ou falso pra uma variável
                           # isso pode ter serventia mais pra frente em IA ou Machine Learning

print("As variáveis booleanas:")                           
print (booleano_verdadeiro) # Mostra True, como foi atribuído a variável

booleano_falso = False # Atribui falso a variável 'booleano_falso'

print (booleano_falso) # Mostra False, como foi atribuído a variável