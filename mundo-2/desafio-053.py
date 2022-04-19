'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Ex.:
- Apos a sopa
- A sacada da casa
- A torre da derrota
- O lobo ama o bolo
'''

# recebendo a frase
f = str(input('Frase: ')).strip()

# removendo os espaços
f1 = f.replace(' ', '').lower()

# lendo o último endereço da frase
u = len(f1)-1

palindromo = True

# lendo de 0 ao último endereço
for i in range(0, len(f1)):
    if f1[i] != f1[u]:
        palindromo = False
    u = u-1

print(f'É palíndromo? {palindromo}')

'''
Outra solução

# do último ao primeiro diminuindo 1
f2 = f1[::-1] 

if f1 == f2:
    print('É palíndromo')
else:
    print('Não é palíndromo')
'''
