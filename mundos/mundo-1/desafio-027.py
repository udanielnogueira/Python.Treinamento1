'''
Faça um programa que leia o nome completo de
uma pessoa, mostrando em seguida o primeiro
e o último nome separadamante.
'''

n = input('Digite seu nome: ').strip()

s = n.split()

print('Primeiro nome:', s[0])
print('Último nome:', s[len(s)-1]) # ou s[-1]
