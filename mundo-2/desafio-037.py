'''
Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual
será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
'''

try:
    n = int(input('Número: '))
except:
    print('Insira um número inteiro')
    exit()

o = input('Deseja converter para qual base?\n1 bin\n2 oct\n3 hex\nOpção: ')

if o == '1':
    print(f'{n:b}')
elif o == '2':
    print(f'{n:o}')
elif o == '3':
    print(f'{n:x}')
else:
    print('Opção inválida')

# ou usar bin(n) oct(n) hex(n)
