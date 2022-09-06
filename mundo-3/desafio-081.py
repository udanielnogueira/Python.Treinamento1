'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos número fora digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []

while True:
    valores.append(int(input('n: ')))

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    else:
        continue

print(f'Foram digitados {len(valores)} valores')

valores.sort(reverse = True)
print(valores)

if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
