'''
Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagam, cobrando
R$0.50 por Km para viagens de até 200Km e R$0.45 
para viagens mais longas.
'''

d = float(input('Distância: '))

if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45

print(f'Custo da viagem: R$ {p:.2f}')
