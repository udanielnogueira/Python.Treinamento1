'''
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

opcao = 0
while opcao != 5:
    print()
    n1 = int(input('Digite o valor 1: '))
    n2 = int(input('Digite o valor 2: '))
    print()

    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print()

    opcao = int(input('Opção: '))

    if opcao == 1:
        print(f'Soma: {n1+n2}')
    elif opcao == 2:
        print(f'Multiplicação: {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        elif n2 > n1:
            print(f'O maior é {n2}')
        else:
            print(f'Os dois são iguais')
    elif opcao == 4:
         continue
    elif opcao != 5:
        print('Opção inválida')
