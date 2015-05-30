n1 = input("Entre com o primeiro numero: ")
n2 = input("Entre com o segundo numero: ")
n3 = input("Entre com o terceira numero: ")

if n1 > n2 and n1 > n3:
   print "%i eh o maior numero." % (n1)
elif n2 > n1 and n2 > n3:
   print "%i eh o maior numero." % (n2)
elif n3 > n1 and n3 > n2:
   print "%i eh o maior numero." % (n3)

if n1 < n2 and n1 < n3:
   print "%i eh o menor numero." % (n1)
elif n2 < n1 and n2 < n3:
   print "%i eh o menor numero." % (n2)
elif n3 < n1 and n3 < n2:
   print "%i eh o menor numero." % (n3)

