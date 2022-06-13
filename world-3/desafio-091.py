'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''

from random import randint
from time import sleep

jogadas = {}
lista_jogadas = []

jogadas['jogador1'] = randint(1,6)
jogadas['jogador2'] = randint(1,6)
jogadas['jogador3'] = randint(1,6)
jogadas['jogador4'] = randint(1,6)

for k, v in jogadas.items():
    print(f'{k}: {v}')
    sleep(1)

for k, v in jogadas.items():
    lista_jogadas.append(v)

lista_jogadas.sort()
print(lista_jogadas)
