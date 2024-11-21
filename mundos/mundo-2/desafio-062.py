'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

# fórmula do termo geral: an = a1 + (n-1) * r

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

add = 1
termos = 10
while add != 0:

    # cálculo do último termo 
    u = p + (termos - 1) * r

    n = p
    while n <= u:
        print(n)
        n = n + r
    
    add = int(input('Mais quantos termos deseja mostrar? '))
    termos = termos + add
