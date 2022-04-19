'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Os dois são iguais
'''

a = int(input('a: '))
b = int(input('b: '))

if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('Os dois são iguais.')
