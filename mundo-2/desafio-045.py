'''
Crie um programa que faça o
computador jogar Jokenpô com você.
'''

import random, time

# Título do jogo
print('\n', end='')
print('='*16)
print('  JOKENPÔ GAME')
print('='*16, end='')
print('\n')

# Escolha do usuário
print('[1] Pedra [2] Papel [3] Tesoura')
u = (input('Escolha: '))

# Escolha do computador
lista = ['1', '2', '3']
random.shuffle(lista)
c = random.choice(lista)

# Animação
print('\n', end='')
print('JO-KEN-PÔ!')
time.sleep(1.20)

# Análise do vencedor
if u == '1' and c == '1':
    print('\nEmpate')
elif u == '1' and c == '2':
    print('\nComputador ganhou!')
elif u == '1' and c == '3':
    print('\nVocê ganhou!')
elif u == '2' and c == '2':
    print('\nEmpate')
elif u == '2' and c == '1':
    print('\nVocê ganhou!')
elif u == '2' and c == '3':
    print('\nComputador ganhou!')
elif u == '3' and c == '3':
    print('\nEmpate')
elif u == '3' and c == '1':
    print('\nComputador ganhou!')
elif u == '3' and c == '2':
    print('\nVocê ganhou!')
else:
    print('\nOpção inválida')

# Escolhas
print('\n', end='')
print(f'Usuário [{u}] Computador [{c}]')

# Sair
print('\n', end='')
input('Pressione ENTER para sair ')
