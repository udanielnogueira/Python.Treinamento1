'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.
'''

valores = []

for contador in range(0,5):
    valores.append(int(input(f'[{contador}] = ')))

for index, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{max(valores)} está na posição {index}')
    elif valor == min(valores):
        print(f'{min(valores)} está na posição {index}')
