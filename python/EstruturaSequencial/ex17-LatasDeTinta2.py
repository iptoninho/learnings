# -- coding: utf-8 --
"""
Faça um Programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadrados da area a ser pintada.
Considere que a cobertura da tinta e de 1 litro para cada 6 metros quadrados e que a tinta e vendida em latas de
18 litros, que custam R$ 80,00 ou em galoes de 3,6 litros, que custam R$ 25,00.

    Informe ao usuario as quantidades de tinta a serem compradas e os respectivos precos em 3 situacoes:
    comprar apenas latas de 18 litros;
    comprar apenas galoes de 3,6 litros;
    misturar latas e galoes, de forma que o preco seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto e, considere latas cheias.
"""
areaPintada = input("Entre com o tamanho em metros da area a ser pintada: ")

lata = 18
custoDaLata = 80

galao = 3.6
custoDoGalao = 25

cobertura = areaPintada / 6

qtdLataDeTinta = areaPintada / lata
qtdGalaoDeTinta = areaPintada / galao	
#qtdDeTinta = 

precoTotalLata = qtdLataDeTinta * custoDaLata
precoTotalGalao = qtdGalaoDeTinta * custoDoGalao
#precoTotal = qtdDeTinta

print "Comprando apenas latas de 18 litros:"
print "Uma area de %i metros, voce precisara de %i lata(s) de tinta." % (areaPintada,round(qtdLataDeTinta))
print "Preco Total: R$ %i" % (precoTotalLata)

print "Comprando apenas galoes de 3.6 litros:"
print "Uma area de %i metros, voce precisara de %i lata(s) de tinta." % (areaPintada,round(qtdGalaoDeTinta)) #round = arredonda o valor para cima'
print "Preco Total: R$ %i " % (precoTotalGalao)

if cobertura >= 18:
   print "Uma area de %i metros, voce precisara de %i lata(s) e %i galao(oes) de tinta." % (areaPintada,round(qtdLataDeTinta),round(qtdGaloesDeTinta))
   print "Preco Total: R$ %i" % (precoTotalLata)
else:
   #qtdTinta = areaPindata - cobertura
   print "Uma area de %i metros, voce precisara de %i galao(oes) de tinta." % (areaPintada,round(qtdGalaoDeTinta))
   print "Preco Total: R$ %i" % (precoTotalGalao)







