'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

# fórmula do termo geral: an = a1 + (n-1) * r

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

# cálculo do último termo 
u = p + (10 - 1) * r

for i in range(p, u+1, r):
    print(i)
