'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[], [], []]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'n: ')))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
