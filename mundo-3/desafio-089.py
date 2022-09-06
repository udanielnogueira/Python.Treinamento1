'''
Crie um programa que leia  nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre uma boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
'''

alunos = []

aluno = []
notas = []

while True:
    nome = str(input('\nNome: '))
    aluno.append(nome)

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas[:])

    aluno.append(media)

    # Append final
    alunos.append(aluno[:])

    aluno.clear()
    notas.clear()

    continuar = str(input('\nDeseja continuar? [s/n] ')).upper()
    if continuar == 'N':
        break

alunos.sort()

print(f'\nLISTA DE ALUNOS')
for i, aluno in enumerate(alunos):
    print(f'{i+1:<2} {aluno[0]:.<20} {aluno[2]:>4.1f}')

while True:
    n = int(input('\nMostrar notas de qual aluno? '))
    print(f'\n{n:<2} {alunos[n-1][0]:.<20} Nota 1: {alunos[n-1][1][0]} Nota 2: {alunos[n-1][1][1]}')
    
    continuar = str(input('\nDeseja continuar? [s/n] ')).upper()
    if continuar == 'N':
        break

'''
Também poderia fazer alunos.append([nome, [nota1, nota2], media])
'''
