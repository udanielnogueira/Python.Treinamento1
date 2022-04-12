'''
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''

import math

# math.sin(x) calcula o seno de x radianos
# logo, preciso transformar o ângulo dado em radianos

ang = int(input('Ângulo: '))
rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print(f'Seno: {sen:.2f}')
print(f'Cosseno: {cos:.2f}')
print(f'Tangente: {tan:.2f}')
