'''
Faça um programa
que leia três números
e mostre qual é o maior
e qual é o menor.
'''

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

'''
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
'''

# descobrindo o menor
if a<b and a<c:
    menor = a
elif b<a and b<c:
    menor = b
else:
    menor = c

# descobrindo o maior
if a>b and a>c:
    maior = a
elif b>a and b>c:
    maior = b
else:
    maior = c

print('O menor é:', menor)
print('O maior é:', maior)
