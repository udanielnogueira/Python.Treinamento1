dados = {}

dados = {'nome':'Pedro', 'idade':'25'}

# Adiciona
dados['sexo'] = 'M'

print(type(dados))

print(dados['nome'])
print(dados)

# Remove
del dados['idade']
print(dados)
