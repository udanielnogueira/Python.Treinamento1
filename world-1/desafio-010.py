'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostra quantos Dólares ela pode comprar.
'''

c = float(input('Quanto você tem na carteira: R$ '))

# April 5th, 2022
d = c / 4.62
e = c / 5.06

print(f'Você pode comprar $ {d:.2f}') # ou US$
print(f'Você pode comprar € {e:.2f}')
