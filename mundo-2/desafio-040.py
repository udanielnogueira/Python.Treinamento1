'''
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0 REPROVADO
- Média entre 5.0 a 6.9 RECUPERAÇÃO
- Média 7.0 ou superior APROVADO
'''

n1 = float(input('n1: '))
n2 = float(input('n2: '))

m = (n1+n2)/2

if m < 5:
    print(f'Média {m} Reprovado')
elif 5 <= m <= 6.9:
    print(f'Média {m} Recuperação')
else:
    print(f'Média {m} Aprovado')
