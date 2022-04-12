'''
Faça um programa que leia um ano
qualquer e mostra se ele é BISSEXTO.

https://mundoeducacao.uol.com.br/matematica/anos-bissextos.htm
'''

a = (input('Ano: '))

n = int(a)

# diz se tem 00 no final
zero = a[-1] == '0' and a[-2] == '0'

print(zero)

if zero and n % 400 == 0:
    print('Ano bissexto') # zero True
elif (zero == False) and n % 4 == 0:
    print('Ano bissexto') # zero False
else:
    print('Ano não é bissexto')

'''
Outra lógica:

if a % 4 == 0 or a % 400 == 0 and a % 100 != 0
'''
