'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de 
fogos de artifício, indo de 10 até O, com uma pausa de 1 segundo entre eles.
'''

from time import sleep

# de 10 a -1 diminuindo 1
for i in range(10, -1, -1): 
    print(i)
    sleep(1)

print('Feliz ano novo!')
