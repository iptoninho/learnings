import random
numero = random.randint(1,100)
tentativas = 0
escolha = 0
while escolha != numero:
    escolha = input('Entre com um valor entr 1 e 100: ')
    tentativas += 1
    if escolha > numero:
        print 'maior'
    elif escolha < numero:
        print 'menor'
    else:
        print '\nParabens, o numero sorteado foi',numero
print "Voce usou", tentativas,'tentativas'
