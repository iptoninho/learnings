#O script abaixo sobrescreve o arquivo
f = open('resources/filewrited.txt','w')
f.write('Hello World\n')
f.close()

#Mesma funcao do script anterior mas sem a necessidade do f.close()
with open('resources/filewrited.txt','w') as out_file:
	out_file.write('Este texto vai para um arquivo\nAbra e veja!\n')
