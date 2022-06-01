'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = ('Cheetos', 2.50,'Doritos', 4.50, 'Baconzitos', 5.00, 'Ruffles', 3.50)

for i in range(0,len(produtos),2):
    print(f'{produtos[i]:.<20} R$ {produtos[i+1]:.2f}')
