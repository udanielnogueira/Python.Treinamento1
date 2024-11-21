'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('CAIXA ELETRÔNICO')
saque = int(input('Valor de saque: R$ ' ))
print()

nota50 = 0
nota20 = 0
nota10 = 0
nota02 = 0

while saque > 1 and saque >= 50:
    saque = saque - 50
    nota50 += 1
    if saque < 50:
        break

while saque > 1 and saque >= 20:
    saque = saque - 20
    nota20 += 1
    if saque < 20:
        break

while saque > 1 and saque >= 10:
    saque = saque - 10
    nota10 += 1
    if saque < 10:
        break

while saque > 1:
    saque = saque - 2
    nota02 += 1
    if saque < 2:
        break

print(f'Notas de R$ 50: {nota50}')
print(f'Notas de R$ 20: {nota20}')
print(f'Notas de R$ 10: {nota10}')
print(f'Notas de R$ 02: {nota02}')

'''
outra forma

nota50 = valor // 50
valor %=  50

nota20 = valor // 20
valor %= 20

nota10 = valor // 10
valor %= 10

nota1 = valor // 1
'''
