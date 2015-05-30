metrosPintados = input("Entre com os metros a serem pintados: ")

coberturaLata = round(18.0 * 6.0) #Uma lata de 18 litros cobre 6 metros
coberturaGalao = round(3.6 * 6.0) #Um galao de 3.6 litros cobre 6 metros

qtdLata = round(metrosPintados / coberturaLata) #A quantidade de latas e igual aos metros a serem pintados por metros cobertos
qtdGalao = round(metrosPintados / coberturaGalao) #A quantidade de galoes e igual aos metros a serem pintados por metros cobertos

print "\n Comprando apenas latas de 18 litros:"
print "Para %i  metros, voce vai precisar de %i lata(s).\n" % (metrosPintados, qtdLata)

print "Comprando apenas galoes de 3.6 litros:"
print "Para %i  metros, voce vai precisar de %i lata(s).\n" % (metrosPintados, qtdGalao)

print "Comprando latas e galoes:"
if metrosPintados < 108:
    print "Para %i  metros, voce vai precisar de %i lata(s).\n" % (metrosPintados, qtdGalao)
elif metrosPintados >= 108 :
    print "Para %i  metros, voce vai precisar de %i lata(s).\n" % (metrosPintados, qtdLata)



