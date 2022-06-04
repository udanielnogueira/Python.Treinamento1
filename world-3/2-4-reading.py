'''
Recebendo elementos e inserindo na lista
'''

combo = []

# Recebendo elementos do usuário
print('Monte seu combo!')
for contador in range(0,5):
    combo.append(str(input(f'Item {contador+1}: ')))

print('Seu combo: ', *combo, sep=' ', end='.')
