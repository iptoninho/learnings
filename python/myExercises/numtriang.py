#verificar se um numero e triangular
num = 10000
i,j,k = 1,2,3
x = 0

while num != 0:
    while i*j*k < x:
        i += 1
        j += 1
        k += 1
    if i*j*k == x:
        print x,'eh trangular'
    #else:
    #    print x,'nao e triangular'
    x = x + 1
    num = num - 1
