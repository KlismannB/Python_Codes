# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, nome, sobremome): # funcão especial que é executada no momento em que a classe é invocada (klismann = Pessoa("Klismann", " Barros"))
        # a varável self apresenta seu próprio objeto (a variável klismann é um objeto de Pessoa)
        self.name = nome # atributo de pessoa
        self.surname = sobremome # atributo de pessoa
    def imprime_nome(self): # método imprime_nome
        return (self.name + self.surname)
    
class Generico(Pessoa):
    def altera_nome(self):
        self.name = self.surname
        
klismann = Pessoa("Klismann", " Barros")

print (klismann.name) # acessando o atributo 'name' definido na classe pessoa
print (klismann.surname)
print (klismann.imprime_nome())

joao = Generico("Joao", " da Silva")
print (joao.name)
joao.altera_nome()

print (joao.name)
print (joao.surname)
print (joao.imprime_nome())