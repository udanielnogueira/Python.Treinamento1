'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre O e 5 e peça para o
usuário tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela
se o usuário venceu ou perdeu.
'''

import random

from time import sleep

x = random.randint(0, 5)

n = int(input('Tente advinhar um número de 0 a 5: '))

print('Processando...')
sleep(2)

if n > 5:
    print('Opção inválida')
elif n == x:
    print(f'Pensei no número {x}, acertou!')
else:
    print(f'Pensei no número {x}, errou!')
