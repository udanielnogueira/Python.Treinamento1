'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

pesoMaior = 0
pesoMenor = 10000
for i in range(1, 6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if peso > pesoMaior:
        pesoMaior = peso
    if peso < pesoMenor:
        pesoMenor = peso

print(f'Menor peso: {pesoMenor:.2f} kg')
print(f'Maior peso: {pesoMaior:.2f} kg')
