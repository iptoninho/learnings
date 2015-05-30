#Utiliazando objeto open chamando a leitura do arquivo com o with
#carregamos todo o arquivo para a memoria, ele faz a leitura e
#fecha o arquivo automaticamente
#esse script executa a mesma funcao do ultimo script mensionsionado
#nesse arquivo, porem nao faz o fechamento do arquivo automaticamente
with open('resources/simple.txt','r') as in_file:
	print(in_file.read())

#Esse script carrega todo o arquivo para a memoria e mostra na tela
#f = open('simple.txt','r')
#print(f.read())

#O script abaixo e a melhor maneira de ler um arquivo, ao passo que
#nao o carrega inteiro para memoria
#f = open('simple.txt','r')
#for line in f:
#print(line)
#f.close()
