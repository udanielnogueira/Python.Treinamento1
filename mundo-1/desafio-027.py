'''
Faça um programa
que leia o nome
completo de uma
pessoa, mostrando em
saguida o primeiro e o
último nome
saparadamante.
'''

n = input('Digite seu nome: ')

s = n.split()

print('Primeiro nome:', s[0])
print('Último nome:', s[len(s)-1])
