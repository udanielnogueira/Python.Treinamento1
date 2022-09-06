'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

import datetime

anoAtual = datetime.date.today().year

maiorIdade = 0
menorIdade = 0
for i in range(0, 7):
    anoNasc = int(input('Ano de nascimento: '))
    idade = anoAtual - anoNasc
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f'Maior idade: {maiorIdade}')
print(f'Menor idade: {menorIdade}')
