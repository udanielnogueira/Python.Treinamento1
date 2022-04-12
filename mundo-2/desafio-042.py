'''
Rafaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais.
- Isóscelas: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''

a = float(input('lado a: '))
b = float(input('lado b: '))
c = float(input('lado c: '))

t = (a+b)>c and (a+c)>b and (b+c)>a

print(a, b, c)

if t:
    if a == b == c:
        print('É um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print('É um triângulo isósceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo')
