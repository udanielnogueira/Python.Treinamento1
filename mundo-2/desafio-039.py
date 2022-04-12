'''
Faça um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar 
o tempo que falta ou que passou.
'''

import datetime

nasc = int(input('Ano de nascimento: '))

atual = datetime.date.today().year

anos = atual - nasc

if anos < 18:
    print(f'Você tem {anos} anos e ainda vai se alistar ao Exército.')
    print(f'Falta {18 - anos} anos.')
elif anos == 18:
    print(f'Você tem {anos} anos e chegou a hora de se alistar ao Exército.')
else:
    print(f'Você tem {anos} anos e já passou da hora de se alistar ao Exército.')
    print(f'Passou {anos - 18} anos.')
