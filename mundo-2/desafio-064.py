'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
'''

numero = 0
acumulador = 0
contador = 0

while numero != 999:
    numero = int(input('n: '))
    if numero != 999:
        acumulador += numero 
        contador += 1

print(f'Foram digitados {contador} números\nSoma: {acumulador}')
