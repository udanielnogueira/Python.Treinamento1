# Criando uma lista de dados
dados = list()

# Adicioando elementos a dados
dados.append('Pedro')
dados.append(25)

# Criando uma lista de pessoas
pessoas = list()

# Adicionando uma cópia de dados a pessoas
pessoas.append(dados[:])

# Uma lista de listas
print(pessoas)
