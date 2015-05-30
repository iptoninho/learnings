def tabuada():
    num = input('Entre com um numero: ')
    i = 1
    while i < 10:
        print '%i * %i = %i' % (num, i, i*num)
        i += 1
    op = input('Gostaria de continuar? ')
    if op == 1:
        tabuada()
    else:
        return False
tabuada()