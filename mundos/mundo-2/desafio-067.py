'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    n = int(input('\nQual tabuada deseja saber? '))
    if n < 0:
        break
    print('='*20)
    print('TABUADA')
    print('='*20)
    for i in range(1, 11):
        print(f'{n} x {i:>2} = {n*i:>2}')
