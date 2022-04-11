'''
Faça um programa
que leia três números
e mostre qual é o maior
e qual é o menor.
'''

n0 = int(input('n1: '))
n1 = int(input('n2: '))
n2 = int(input('n3: '))

lista = [n0, n1, n2]

if lista[0] > lista[1]:
    lista[0] = n1
    lista[1] = n0 
    if lista[1] > lista[2]:
        lista[1] = n2
        lista[2] = n0
        if lista[0] > lista[1]:
            lista[0] = n2
            lista[1] = n1
else:
    print('',end='')

print('O maior é:', lista[2])
print('O menor é:', lista[0])
