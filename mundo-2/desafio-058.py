'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
'''

import random
from time import sleep

acertou = False
tentativas = 0

while acertou == False:
    x = random.randint(0, 10)
    n = int(input('Tente advinhar um número de 0 a 10: '))

    '''
    print('Processando...')
    sleep(0.5)
    '''

    if n > 10:
        print('Opção inválida')
    elif n == x:
        print(f'Pensei no número {x}, acertou!')
        acertou = True
        tentativas += 1
    else:
        print(f'Pensei no número {x}, errou!')
        tentativas += 1

print(f'Número de tentativas: {tentativas}')
