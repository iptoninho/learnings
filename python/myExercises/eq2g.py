import math
a = input('Entre com o valor de a: ')
b = input('Entre com o valor de b: ')
c = input('Entre com o valor de c: ')

if a == 1:
	eq2g = '\nx^2'+str(b)+'x'+str(c)+'= 0'
else:
	eq2g = '\n'+str(a)+'x^2'+str(b)+'x'+str(c)+'= 0'

print eq2g

delta = (b**2)-(4*a*c)
print 'delta =','(',a,'^2',') - (4 *',a,'*',c,')\n'

if b**2 > 0:
	sinal='+'

print 'delta =',b**2,sinal,(-4*a*c)
print 'delta =',delta,'\n'

x1 = (-b + math.sqrt(delta))/2*a
x2 = (-b - math.sqrt(delta))/2*a

print 'x1 =',-b + math.sqrt(delta),'/ 2 *', a
print 'x1 =',-b + math.sqrt(delta),'/',2*a
print 'x1 =',x1,'\n'

print 'x2 =',-b - math.sqrt(delta),'/ 2 *', a
print 'x2 =',-b - math.sqrt(delta),'/',2*a
print 'x2 =',x2,'\n--------------------------'

print(eq2g)
print 'delta =',delta
print 'x1 =',x1
print 'x2 =',x2,'\n'
