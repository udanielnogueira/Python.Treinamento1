'''
Crie um programa
que leia um número
Real qualquer pelo
teclado a mostre na
tela a sua porção
Inteira.
'''

from math import trunc

n = float(input('Número real: '))

print(f'Parte inteira: {trunc(n)}')
