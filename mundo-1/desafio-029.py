'''
Escreva um
programa que leia a
velocidade de um
carro.

Sa ele ultrapassar
80km/h, mostre uma
mensagam dizendo
que ele foi multado.

A multa vai custar
RS7.00 por cada Km
acima do limite.
'''

v = float(input('Velovidade do carro: '))

if v > 80:
    d = v - 80
    m = 7 * d
    print(f'Você foi multado, pague R$ {m:.2f}')
else:
    print('Você está dentro do limite de velocidade')
