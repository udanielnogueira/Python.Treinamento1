'''
Um professor quer
sortear um dos seus
quatro alunos para
apagar o quadro. Faça
um programa qua ajude
ele, lendo o nome deles
e escrevendo o nome
do escolhido.
'''

import random

n1 = str(input('Insira o nome do aluno: '))
n2 = str(input('Insira o nome do aluno: '))
n3 = str(input('Insira o nome do aluno: '))
n4 = str(input('Insira o nome do aluno: '))

lista = [n1, n2, n3, n4]

x = random.choice(lista)

print(f'Aluno(a) sorteado(a): {x}')
