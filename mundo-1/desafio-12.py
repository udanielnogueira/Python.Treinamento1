'''
Faça um algoritmo
que leia o preço de um
produto e mostre seu
novo preço, com 5% de
desconto.
'''

p = float(input('Preço do produto: '))

d = p*0.05

newP = p-d

print(f'Valor com desconto: {newP:.2f}')
