'''
Faça um programa
que leia uma frase pelo
teclado e mostre:

Quantas vezes
aparece a letra "A".

Em que posição ela
aparece a primeira
vez.

Em que posição ela
aparece a última vez.
'''

f = input('Digite uma frase: ').strip()

f1 = f.upper().replace('Á', 'A').replace('Ã', 'A').replace('Â', 'A')

# print(f1)

print(f'A letra a aparece {f1.count("A")} vezes na frase.')

print(f'Primeira posição de a: {f1.find("A")}')

print(f'A última posição de a: {f1.rfind("A")}')
