'''
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

s=0
# múltiplos de 3
for i in range(3, 500, 3):
    # que não sejam par
    if (i % 2) != 0:
        print(i)
        s += i 

print(f'Somatório: {s}')
