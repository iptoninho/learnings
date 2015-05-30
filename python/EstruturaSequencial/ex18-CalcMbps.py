filesize = input("Entre com o tamanho do arquivo a ser baixado(em MB): ")
link = input("Entre com a velocidade do seu link de Internet(em Mbps): ")

link = link * 0.1
segDown = filesize / link
minDown = segDown / 60.0
hourDown = minDown / 60.0

print "Com um link de %i Mbps, voce baixara um arquivo %i Mb(s) em %i segundo(s)." % (link,filesize,segDown)
print "Com um link de %i Mbps, voce baixara um arquivo %i Mb(s) em %i minuto(s)." % (link,filesize,minDown)
print "Com um link de %i Mbps, voce baixara um arquivo %i Mb(s) em %.2f hora(s)." % (link,filesize,hourDown)





