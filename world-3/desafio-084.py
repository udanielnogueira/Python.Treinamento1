'''
Crie um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
'''

pessoas = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    pessoas.append(dados[:])

    dados.clear()

    continuar = str(input('Continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    else:
        continue

pessoas_leves = list()
pessoas_pesadas = list()

for pessoa in pessoas:
    if pessoa[1] <= 70:
        pessoas_leves.append(pessoa[:])
    elif pessoa[1] >= 100:
        pessoas_pesadas.append(pessoa[:])

print(len(pessoas))
print(pessoas_leves)
print(pessoas_pesadas)
