'''
Faça um programa
que leia o comprimento
do cateto oposto e do
cateto adjacente de um
triângulo retângulo.
Calcule e mostre o 
comprimento da 
hipotenusa.
'''

import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

print(f'Hipotenusa: {math.hypot(ca, co):.3f}')
