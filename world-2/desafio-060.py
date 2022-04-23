'''
Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

n = int(input('n: '))

fat = 1
while n >= 1:
    fat = fat * n
    n = n - 1

print(f'Fatorial: {fat}')
