"""Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.
   Calcule e mostre o total do seu salario no referido mes, sabendo-se que sao descontados 11% para
   o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faca um programa que nos de:

    salario bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salario liquido.
    calcule os descontos e o salario liquido, conforme a tabela abaixo:

    + Salario Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salario Liquido : R$

    Obs.: Salario Bruto - Descontos = Salario Liquido. 
"""

salhr = input("Entre com o valor ganho por hora: ")
numhr = input("Entre com o numero de horas trabalhadas no mes: ")

salbrt = salhr * numhr

ir = salbrt * 0.11
inss = salbrt * 0.08
sindicato = salbrt * 0.05

descontos = ir + inss + sindicato
salliq = salbrt - descontos

print "\n+ Salario Bruto : R$ %.2f" %(salbrt)
print "- IR(11) : R$ %.2f" % (ir)
print "- INSS(8) : R$ %.2f" % (inss)
print "- Sindicado(5) : R$ %.2f" % (sindicato)
print "= Salario Liquido : %.2f\n" % (salliq)
