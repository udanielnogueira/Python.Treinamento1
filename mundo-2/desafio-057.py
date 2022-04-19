'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = 'A'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('[M/F] Sexo: ')).upper()
