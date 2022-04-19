'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
'''

# fórmula do termo geral: an = a1 + (n-1) * r

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# cálculo do último termo 
u = p + (10 - 1) * r

n = p
while n <= u:
    print(n)
    n = n + r
