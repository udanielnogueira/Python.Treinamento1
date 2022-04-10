'''
Faça um programa
que leia um número de
de 0 a 9999 e mostre na
tela cada um dos
dígitos separados.

1834
milhar: 1
centena: 8
dezena: 3
unidade: 4
'''

n = int(input('Digite um número: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
