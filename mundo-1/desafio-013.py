'''
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário com 15% de aumento.
'''

s = float(input('Salário: R$ '))

a = s * 0.15

newS = s + a

print(f'Novo salário: R$ {newS:.2f}')
print(f'Aumento de R$ {a:.2f} no salário')
