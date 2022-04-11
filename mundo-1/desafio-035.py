'''
Desenvolva um
programa que leia o
comprimento de três
retas e diga ao usuário
se elas podem ou não
formar um triângulo.

'''

r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

'''
Condição de existência de um triângulo

A soma das medidas de dois dos lados
sempre será maior que a terceira medida.
'''

if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
    print('As retas formam um triângulo.')
else:
    print('As retas não formam um triângulo.')
