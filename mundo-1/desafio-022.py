'''
Crie um programa
que leia o nome
completo de uma
pessoa e mostre:

O nome com todas as
letras maiúsculas.

O nome com todas as
letras minúsculas.

Quantas letras ao todo 
(sem considerar espaços).

Quantas letras tem o
primeiro nome.
'''

nome = input('Digite seu nome: ')

print(nome.upper())

print(nome.lower())

print('Quantidade de caracteres (com espaço):', len(nome))
print('Quantidade de caracteres (sem espaço):', len(nome) - nome.count(' '))

print('Quantidade de caracteres do primeiro nome:', len(nome.split()[0]))
