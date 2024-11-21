'''
Escreva um programa que pergunte o salário de um Funcionário e
calcule o valor do seu aumento. Para salários superiores a
RS1.250.00, calcule um aumento de 10%. Para os inferiores
ou iguais, o aumento é da 15%.
'''

s = float(input('Salário R$ '))

if s > 1250:
    a = s * 0.10
else:
    a = s * 0.15

print(f'Aumento de R$ {a}')
print(f'Novo salário R$ {s+a}')
