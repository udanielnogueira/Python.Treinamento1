'''
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

totalGasto = 0
maisMil = 0
barato = 10**100
produtoBarato = ' '

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))

    totalGasto += preco

    if preco > 1000:
        maisMil += 1
    
    if preco < barato:
        barato = preco
        produtoBarato = produto

    continuar = str(input('Continuar? [S/N]: ')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opção inválida')
        break

print(f'Total gasto: R$ {totalGasto}')
print(f'Custam mais de R$ 1 Mil: {maisMil} produtos')
print(f'Produto mais barato: {produtoBarato}')
