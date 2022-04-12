'''
Faça um programa que leia um número Inteiro
qualquer e mostre na tela a sua tabuada.
'''

n = int(input('Digite um número: '))

msg = 'TABUADA'
print(f'\n{msg:=^25}') # símbolo + alinhamento + espaços

print(f'{n} x {1:2} = {n*1}') # não precisa do >, 2 espaços já alinha à direita 
print(f'{n} x {2:2} = {n*2}')
print(f'{n} x {3:2} = {n*3}')
print(f'{n} x {4:2} = {n*4}')
print(f'{n} x {5:2} = {n*5}')
print(f'{n} x {6:2} = {n*6}')
print(f'{n} x {7:2} = {n*7}')
print(f'{n} x {8:2} = {n*8}')
print(f'{n} x {9:2} = {n*9}')
print(f'{n} x {10} = {n*10}')

print('='*25)

# caso dê mais espaços, alinhamento volta ao padrão
