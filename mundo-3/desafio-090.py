'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))

if alunos['média'] > 5:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'

for k, v in alunos.items():
    print(f'{k.title()} é {v}.')
