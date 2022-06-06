'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. o programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.
'''

from random import randint
from time import sleep

quantidade_jogos = int(input('Jogos a serem gerados? '))

# Uma futura lista de listas 
jogos = []

numeros = []

for i in range(0,quantidade_jogos):
    while True:
        aleatorio = randint(1,60)
        
        # Em um mesmo jogo, não há repetição
        if aleatorio not in numeros:
            numeros.append(aleatorio)
        if len(numeros) == 6:
            break
    jogos.append(numeros[:])
    numeros.clear()

for i, jogo in enumerate(jogos):
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)
