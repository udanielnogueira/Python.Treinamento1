'''
Desenvolva um programa que leia quatro valores pelo teclado e gurade-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.

b) Em que posição foi digitado o primeiro valor 3.

c) Quais foram os números pares.
'''

n = [0,0,0,0]

for i in range(0,4):
    n[i] = int(input('n: '))

tupla = (n[0], n[1], n[2], n[3])

print(type(tupla))
print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vez(es)')

if 3 in tupla:
    print(f'O número 3 aparece primeiro na {tupla.index(3)+1}º posição')
else:
    print('O número 3 não aparece em nenhuma posição')

print('Os números pares foram: ', end='')
for x in tupla:
    if x % 2 == 0:
        print(f'{x} ', end='')
