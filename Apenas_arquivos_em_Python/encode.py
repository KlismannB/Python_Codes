nome = "Klismann Barros"
codificado = nome.encode("base64")
decodificado = codificado.decode("base64")
print ("Nome = {}" .format(nome))
print ("Nome codificado em base64 = {}" .format(codificado))
print ("Nome decodificado da base64 = {}" .format(decodificado))
