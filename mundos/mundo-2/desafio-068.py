'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

import random

vitorias = 0
while True:
    computador = random.randint(0, 10)
    jogador = int(input('Digite um valor: '))
    resultado = computador + jogador

    parImpar = str(input('Par ou ímpar? [p/i]: ')).upper()

    if resultado % 2 == 0:
        if parImpar == 'P':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu')
            print(f'Computador:{computador} jogador:{jogador} Resultado:{resultado}')
            break
    else:
        if parImpar == 'I':
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu')
            print(f'Computador:{computador} jogador:{jogador} Resultado:{resultado}')
            break
    print(f'Computador:{computador} jogador:{jogador} Resultado:{resultado}')
    print()

print(f'Total de vitórias: {vitorias}')
