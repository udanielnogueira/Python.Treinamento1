'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valors ímpares 
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

valores = []

while True:
    valores.append(int(input('n: ')))

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    else:
        continue

pares = []
impares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Lista: {valores}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
