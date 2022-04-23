'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que
o usuário escolher. Só que agora utilizando um laço for.
'''
n = int(input('Valor: '))

print('='*12)
print('TABUADA')
print('='*12)

for i in range(0, 11):
    print(f'{n} x {i:2} = {n*i:2}') # :2 usa 2 dígitos de espaço
