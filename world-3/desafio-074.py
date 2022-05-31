'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(type(numeros))

print(numeros)

maior = 0
for x in numeros:
    if x > maior:
        maior = x

menor = 100
for x in numeros:
    if x < menor:
        menor = x

print(f'O maior número da tupla é: {maior}')
print(f'O menor número da tupla é: {menor}')
