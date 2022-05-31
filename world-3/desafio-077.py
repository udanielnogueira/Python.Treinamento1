'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('pizza', 'chocolate', 'doritos', 'coquinha')

vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'{palavra} tem as vogais: ',end='')
    for letra in palavra:
        if letra in vogais:
            print(f'{letra} ', end='')
    print()
