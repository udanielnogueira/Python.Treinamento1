'''
Faça um programa
que leia um ano
qualquer e mostra se
ela é BISSEXTO.

https://mundoeducacao.uol.com.br/matematica/anos-bissextos.htm
'''

a = (input('Ano: '))

n = int(a)

zero = a[-1] == '0' and a[-2] == '0'
# diz se tem 00 no final

print(zero)

if zero and n % 400 == 0:
    print('Ano bissexto') # zero True
elif (zero == False) and n % 4 == 0:
    print('Ano bissexto') # zero False
else:
    print('Ano não é bissexto')
