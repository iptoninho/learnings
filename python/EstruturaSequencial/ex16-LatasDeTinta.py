"""
Faca um programa para uma loja de tintas. O programa devera pedir o tamanho em metros quadrados da area a ser pintada.
Considere que a cobertura da tinta e de 1 litro para cada 3 metros quadrados e que a tinta e vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuario a quantidades de latas de tinta a serem compradas e o preco total. 
"""

areaPintada = input("Entre com o tamanho em metros da area a ser pintada: ")

lata = 18
cobertura = areaPintada / 3
custoDaLata = 80

qtdLataDeTinta = areaPintada / lata
precoTotal = qtdLataDeTinta * custoDaLata

print "Para pintar uma area de %i metros, voce precisara de %i lata(s) de tinta." % (areaPintada,qtdLataDeTinta)
print "Preco Total: R$ %i" % (precoTotal)





