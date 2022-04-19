'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

# divisíveis apenas por 1 e ele mesmo

n = int(input('n: '))

p = True
for i in range(2, n):
    if (n % i) == 0:
        p = False

print(f'{n} é primo? {p}')
