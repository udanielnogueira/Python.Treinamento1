frase = 'Python classes'

# tamanho
print(len(frase))

# conta o caracter
print(frase.count('s'))

# conta do 0 ao 7, excluindo 8
print(frase.count('s',0,8))

# em qual posição encontrou o 'on'
# retorna -1 quando não encontrado
print(frase.find('on'))
print(frase.find('algo'))

#retorna True ou False
print('Python' in frase)
