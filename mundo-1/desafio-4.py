'''
Faça um programa
qua leia algo pelo
teclado e mostre na
tela o seu tipo
primitivo e todas as
informações possíveis
sobre ele.
'''

x = input('Digite algo: ')

print('Tipo?', type(x))
print('Numérico?', x.isnumeric())
print('Alfa?', x.isalpha())
print('Alfanumérico?', x.isalnum())
print('Maiúsculo?', x.isupper())
print('Minúsculo?', x.islower())
print('Espaços?', x.isspace())
