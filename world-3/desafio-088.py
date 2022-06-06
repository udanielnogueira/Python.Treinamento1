'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. o programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.
'''

from random import randint

quantidade_jogos = int(input('Jogos a serem gerados? '))

# Uma futura lista de listas 
jogos = []

# Uma lista
numeros = []

for i in range(0,quantidade_jogos):
    for i in range(0,6):
        numeros.append(randint(1,60))
    jogos.append(numeros[:])
    numeros.clear()

for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
