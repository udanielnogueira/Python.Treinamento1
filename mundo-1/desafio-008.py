'''
Escreva um 
programa que leia um 
valor em metros e o 
exiba convertido em 
centímetros e milímetros.
'''

m = float(input('Digite o valor em metros: '))

cm = m*100
mm = m*1000

print(f'Cm: {cm:.2f}')
print(f'Mm: {mm:.2f}')
