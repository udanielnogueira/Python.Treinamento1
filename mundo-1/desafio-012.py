'''
Faça um algoritmo
que leia o preço de um
produto e mostre seu
novo preço, com 5% de
desconto.

-----------
15% de 875
-----------
875*15/100 ou 875*0,15
'''

p = float(input('Preço do produto: '))

d = p*0.05 # ou d = p*5/100

newP = p-d

print(f'Valor com desconto de 5%: {newP:.2f}')
