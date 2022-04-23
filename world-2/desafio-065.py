'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
'''

continuar = 'S'
acumulador = 0
contador = 0
numero = 0
media = 0
maior = 0
menor = 9*100
while continuar == 'S':
    numero = int(input('n: '))

    acumulador += numero
    contador += 1
    media = acumulador/contador

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    continuar = input('Deseja continuar? [S/N]: ').upper()

media = acumulador/contador

print('média: ', media)
print('maior: ', maior)
print('menor: ', menor)