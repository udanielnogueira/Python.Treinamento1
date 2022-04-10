'''
Faça um programa
que leia uma frase pelo
teclado e mostre:

Quantas vezes
aparece a letra "A".

Em que posição ela
aparece a primeira
vez.

Em que posição ela
aparece a última vez.
'''

f = input('Digite uma frase: ')

i = 0
while i < len(f):
    if f[i] == 'a' or f[i] == 'A':
        print(f'a na posição {i}')
    i = i+1
