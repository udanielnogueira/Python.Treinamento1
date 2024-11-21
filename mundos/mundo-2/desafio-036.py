'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, salário do comprador e em quantos anos ela vai pagar. Calcule o valor da prestação
mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

v = float(input('Valor da casa: '))
s = float(input('Salário: '))
a = int(input('Pagará em quantos anos? '))

m = a * 12
 
p = v / m

if p > (s * 0.3):
    print(f'Prestações de R$ {p:.2f}\nEmpréstimo negado.')
else:
    print(f'Prestações de R$ {p:.2f}\nEmpréstimo aceito.')
