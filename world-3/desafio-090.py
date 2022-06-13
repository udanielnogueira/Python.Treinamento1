'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))

if alunos['media'] > 5:
    alunos['situacao'] = 'Aprovado'
else:
    alunos['situacao'] = 'Reprovado'

print(alunos)
