"""
Joao Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diario de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de Sao Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. Joao precisa que voce faca um programa que leia a
variavel peso (peso de peixes) e verifique se ha excesso. Se houver, gravar na variavel excesso e na variavel multa
o valor da multa que Joao devera pagar. Caso contrario mostrar tais variaveis com o conteudo ZERO. 
"""

peso = input("Entre com o valor em kg de peixe pescado: ")

if peso > 50.0:
   excesso = peso - 50.0
   multa = excesso * 4.0
   print "%.2f kg de peixe geram um exesso de %.2f e %.2f de multa." %(peso,excesso,multa)
else:
   excesso = 0
   multa = 0
   print "%.2f kg de peixe geram um excesso de %.2f e %.2f de multa." %(peso,excesso,multa)




