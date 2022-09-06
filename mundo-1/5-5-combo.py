frase = 'Its now or never'

# contando O maiúsculo
print('O maiúsculo:', frase.count('O'))

# contando O maiúsculo com o upper()
print('O maiúsculo com upper:', frase.upper().count('O'))

frase2 = '   League of Legends   '

# tamanho
print('Tamanho normal:', len(frase2))

# tamanho sem espaços da direita e esquerda
print('Tamanho sem espaços:', len(frase2.strip()))
