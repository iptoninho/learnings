#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Fa�a um programa que verifique se uma letra digitada � vogal ou consoante."""

v1 = raw_input("Insira uma letra: ")
v1 = v1.upper()

if v1 in ('AEIOU'):
   print 'Vogal.\n'
else:
   print 'Consoante.\n'
