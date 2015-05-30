metrosPintados = input("Entre com os metros a serem pintados: ")
cobertura = round(18.0 * 3.0) #Uma lata de 18 litros cobre 3 metros
qtdLata = round(metrosPintados / cobertura) #A quantidade de latas e igual aos metros a serem pintados por metros cobertos

print "Para %i  metros, voce vai precisar de %i lata(s)." % (metrosPintados, qtdLata)


