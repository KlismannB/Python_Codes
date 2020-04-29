nome_completo = "Klismann Barros"
nome_completo_aspas = """Klismann
de
Oliveira
Barros"""
nome_completo_quebra = "Klismann \
de \
Oliveira \
Barros"
nome = "Klismann"
sobrenome = "Barros"
print "Nome completo (1a forma): ", nome_completo
print "Nome completo (2a forma): " + nome_completo
print "Nome completo (3a forma): " + "Klismann" + "de" + "Oliveira" + "Barros"
print "Nome completo (4a forma): " + "Klismann", "de" + "Oliveira", "Barros"
print "Nome completo (5a forma): ", nome_completo_aspas
print "Nome completo (6a forma): ", nome_completo_quebra
print "Nome completo (7a forma): %s" %nome_completo
print "Nome completo (8a forma): %s %s" %(nome, sobrenome)
print "Nome repetido duas vezes: ", nome_completo * 2
