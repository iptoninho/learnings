#!/usr/bin/python
#-*- coding: utf-8 -*-
nota1 = input("Entre com sua primeira nota: ")
nota2 = input("Entre com sua segunda nota: ")

media = (nota1 + nota2) / 2.0

if media == 10:
   print "Media %.1f" % (media)
   print "Aprovado com louvor!"
elif media < 7:
   print "Media %.1f" % (media)
   print "Retido."
elif media >= 7:
   print "Media %.1f" % (media)
   print "Aprovado."

