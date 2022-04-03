'''
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão

Ordem de precedência
1 ()
2 **
3 * / // % (caso conflite, resolva quem aparece primeiro)
4 + -
'''

x = 5+3*2
print(x)

y = 3*5+4**2
print(y)

z = 3*(5+4)**2
print(z)

alfa = 17//2
beta = 17%2
print('17/2 divisão inteira = {} resto = {}' .format(alfa, beta))

uau = 365**522
print('olha isso {}' .format(uau))
