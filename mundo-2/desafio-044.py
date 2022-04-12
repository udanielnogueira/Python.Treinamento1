'''
Elabore um programa que calcula o valor a ser
pago por um produto, considerando o seu preço 
normal e a condição de pagamanto:

- À vista dinheiro ou cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
'''

p = float(input('Valor do produto R$ '))

print('[1] À vista [2] Parcelado')
x = input('Opção: ')

if x == '1':
    print('[1] Dinheiro ou cheque [2] Cartão')
    y = input('Opção: ')
    if y == '1':
        final = p - (p*0.1)
    elif y == '2':
        final = p - (p*0.05)
    else:
        print('Opção inválida')
        exit()

elif x == '2':
    print('[1] Até 2x [2] 3x ou mais')
    y = input(('Opção: '))
    if y == '1':
        final = p
    elif y == '2':
        final = p  + (p*0.2)
    else:
        print('Opção inválida')
        exit()

else:
    print('Opção inválida')
    exit()

print(f'Valor a ser pago: R$ {final:.2f}')
