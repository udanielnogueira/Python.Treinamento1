'''
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''

import datetime

n = int(input('Ano de nascimento: '))

a = datetime.date.today().year

i = a - n

if i <= 9:
    print(f'Idade: {i} Categoria Mirim')
elif i <= 14:
    print(f'Idade: {i} Categoria Infantil')
elif i <= 19:
    print(f'Idade: {i} Categoria Junior')
elif i <= 20:
    print(f'Idade: {i} Categoria Sênior')
else:
    print(f'Idade: {i} Categoria Master')
