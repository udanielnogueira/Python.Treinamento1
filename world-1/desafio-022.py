'''
Crie um programa que leia o nome
completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras tem o seu primeiro nome.
Quantas letras tem sem considerar espaços.
'''

nome = input('Digite seu nome: ').strip() # elimina espaços antes e depois

print(nome.upper())

print(nome.lower())

print('Quantidade de caracteres (com espaço):', len(nome))
print('Quantidade de caracteres (sem espaço):', len(nome) - nome.count(' '))

print('Quantidade de caracteres do primeiro nome:', len(nome.split()[0]))
