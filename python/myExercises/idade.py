n = int(input('Digite o numero de pessoas: '))
cont = 0
while cont < n:
    #nome = input('Digite seu nome: ')
    dia = int(input('Digite o dia de nascimento da pessoa %i: '%(cont+1)))
    mes = int(input('Digite o mes de nascimento da pessoa %i: '%(cont+1)))
    ano = int(input('Digite o ano de nascimento da pessoa %i: '%(cont+1)))
    idade = int(input('Digite a idade a ser completada da pessoa %i: '%(cont+1)))

    #print 'Voce fara',idade,'anos em',dia,'/',mes,'/',ano + idade
    print 'voce fara %i anos em %i/%i/%i\n'%(idade,dia,mes,ano+idade)
    cont += 1
