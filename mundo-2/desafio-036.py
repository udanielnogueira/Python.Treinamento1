'''
Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ela vai 
pagar. Calcule o valor da prestação mensal, sabendo 
que ela não pode exceder 30% do salário ou então o
empréstimo será negado.
'''

v = float(input('Valor: '))
s = float(input('Salário: '))
a = int(input('Pagará em quantos anos? '))

m = a * 12
 
p = valor / m

if p > (s * 0.3):
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')
