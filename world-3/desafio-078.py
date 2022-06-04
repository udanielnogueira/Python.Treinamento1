'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.
'''

valores = []

for contador in range(0,5):
    valores.append(int(input(f'[{contador}] = ')))

print(f'Maior valor: {max(valores)}')
print(f'Menor valor: {min(valores)}')

for index, valor in enumerate(valores):
    print(f'{valor} está no endereço {index}')
